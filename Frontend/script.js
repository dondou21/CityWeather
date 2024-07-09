const apiKey = 'YOUR_API_KEY'; // Replace with your API key from OpenWeatherMap

async function getWeather() {
    const cityInput = document.getElementById('city-input').value;
    const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${cityInput}&units=metric&appid=${apiKey}`;

    try {
        const response = await fetch(apiUrl);
        const weatherData = await response.json();

        // Update UI with weather data
        document.getElementById('city-name').textContent = weatherData.name;
        document.getElementById('temperature').textContent = `Temperature: ${weatherData.main.temp} °C`;
        document.getElementById('description').textContent = `Description: ${weatherData.weather[0].description}`;
    } catch (error) {
        console.error('Error fetching weather data:', error);
        alert('Failed to fetch weather data. Please try again.');
    }
}
