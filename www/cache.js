/**
 * Cache module for storing plant identification results
 * Uses LocalStorage to cache identified plants and create history
 */

// Maximum number of history items to store
const MAX_HISTORY_ITEMS = 10;

// Key for storing history in LocalStorage
const HISTORY_STORAGE_KEY = 'plantIdHistory';

/**
 * Save plant identification result to cache
 * @param {File} imageFile - The image file
 * @param {Object} result - The identification result
 */
function saveToCache(imageFile, result) {
    try {
        // Get existing history
        const history = getHistoryItems();
        
        // Convert image to data URL to store
        const reader = new FileReader();
        reader.onload = function(e) {
            const imageDataUrl = e.target.result;
            
            // Create new history item
            const newItem = {
                id: generateId(),
                image: imageDataUrl,
                result: result,
                date: Date.now()
            };
            
            // Add to history (at the beginning)
            history.unshift(newItem);
            
            // Limit history size
            const limitedHistory = history.slice(0, MAX_HISTORY_ITEMS);
            
            // Save to LocalStorage
            localStorage.setItem(HISTORY_STORAGE_KEY, JSON.stringify(limitedHistory));
        };
        
        reader.readAsDataURL(imageFile);
    } catch (error) {
        console.error('Error saving to cache:', error);
    }
}

/**
 * Get history items from LocalStorage
 * @returns {Array} - Array of history items
 */
function getHistoryItems() {
    try {
        const historyJson = localStorage.getItem(HISTORY_STORAGE_KEY);
        return historyJson ? JSON.parse(historyJson) : [];
    } catch (error) {
        console.error('Error retrieving history:', error);
        return [];
    }
}

/**
 * Check if an image is in the cache
 * This uses a simple hash-based approach to check for similar images
 * @param {File} imageFile - The image file to check
 * @returns {Object|null} - The cached result or null if not found
 */
function checkImageInCache(imageFile) {
    // In a real application, we would use image hashing to detect similar images
    // For this demo, we'll just return null to ensure we always make a fresh API call
    return null;
}

/**
 * Generate a unique ID for history items
 * @returns {string} - A unique ID
 */
function generateId() {
    return Date.now().toString(36) + Math.random().toString(36).substr(2);
}
