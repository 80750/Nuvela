async function getOpenAIKey() {
    try {
        // In a real-world application, this would make a request to a secure server endpoint
        // For the purpose of this demo, we're using a method that doesn't expose the key in client-side code
        return process.env.OPENAI_API_KEY || '';
    } catch (error) {
        console.error('Error retrieving API key:', error);
        throw new Error('Failed to retrieve API key. Please try again later.');
    }
}

// Export the function
export { getOpenAIKey };