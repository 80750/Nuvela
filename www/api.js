const PLANT_ID_API_URL = 'https://plant.id/api/v3';

// Plant.id API key (should be passed in environment variables in a production setup)
// This is a placeholder - in a real application, this would be retrieved securely
// For example, from server-side code or environment variables
const API_KEY = 'DOPotV2JdENYAmaLqWEcGb9i8qVFGGBAVHLWJvxUsxNInhBP1r'; // Replace with actual API key when deploying

/**
 * Identify a plant from an image file
 * @param {File} imageFile - The image file to identify
 * @returns {Promise<Object>} - The identification results
 */
async function identifyPlant(imageFile) {
    try {
        // Convert image to base64
        const base64Image = await fileToBase64(imageFile);
        
        // Prepare API request data
        const data = {
            api_key: API_KEY,
            images: [base64Image.split(',')[1]], // Remove the data URL prefix
            modifiers: ["crops_fast", "similar_images"],
            plant_language: "en",
            plant_details: [
                "common_names",
                "url",
                "wiki_description",
                "taxonomy",
                "synonyms",
                "watering",
                "sunlight",
                "propagation",
                "growth_habit",
                "hardiness"
            ]
        };
        
        // Send API request
        const response = await fetch(PLANT_ID_API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        // Handle API errors
        if (!response.ok) {
            const errorText = await response.text();
            throw new Error(`API error: ${response.status} ${errorText}`);
        }
        
        // Parse API response
        const result = await response.json();
        
        // Validate API response
        if (!result.suggestions || result.suggestions.length === 0) {
            throw new Error('Could not identify this plant. Please try with a clearer image.');
        }
        
        // Process API response into a nicer format
        return processPlantData(result);
        
    } catch (error) {
        console.error('Plant identification error:', error);
        throw new Error('Failed to identify the plant. Please check your internet connection and try again.');
    }
}

/**
 * Process the raw API response into a more usable format
 * @param {Object} apiResponse - The raw API response
 * @returns {Object} - The processed plant data
 */
function processPlantData(apiResponse) {
    const suggestion = apiResponse.suggestions[0];
    const details = suggestion.plant_details;
    
    // Extract common name
    let plantName = suggestion.plant_name;
    if (details.common_names && details.common_names.length > 0) {
        plantName = details.common_names[0];
    }
    
    // Create a description from the wiki data
    let description = 'No description available.';
    if (details.wiki_description && details.wiki_description.value) {
        description = details.wiki_description.value;
    }
    
    // Extract care information
    const sunlightNeeds = details.sunlight && details.sunlight.length > 0 
        ? details.sunlight.join(', ') 
        : 'Medium to bright indirect light';
    
    const wateringNeeds = details.watering 
        ? details.watering 
        : 'Allow soil to dry between watering';
    
    // Build result object
    return {
        plantName: plantName,
        scientificName: suggestion.plant_name,
        confidence: suggestion.probability,
        description: description,
        care: {
            sunlight: sunlightNeeds,
            watering: wateringNeeds,
            temperature: getTemperatureInfo(details),
            soil: getSoilInfo(details)
        }
    };
}

/**
 * Extract temperature information from plant details
 * @param {Object} details - The plant details from API
 * @returns {string} - The temperature information
 */
function getTemperatureInfo(details) {
    if (details.hardiness && details.hardiness.min && details.hardiness.max) {
        return `${details.hardiness.min}°F to ${details.hardiness.max}°F`;
    }
    
    return '65°F to 80°F (18°C to 27°C)';
}

/**
 * Extract soil information from plant details
 * @param {Object} details - The plant details from API
 * @returns {string} - The soil information
 */
function getSoilInfo(details) {
    if (details.soil && details.soil.length > 0) {
        return details.soil.join(', ');
    }
    
    return 'Well-draining potting mix';
}

/**
 * Convert a file to base64 data URL
 * @param {File} file - The file to convert
 * @returns {Promise<string>} - The base64 data URL
 */
function fileToBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}
