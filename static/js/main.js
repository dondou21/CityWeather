document.getElementById('weather-form').addEventListener('submit', function(e) {
    e.preventDefault();
    const city = document.getElementById('city').value;
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('error-message').innerText = data.error;
                document.getElementById('error-message').style.display = 'block';
                document.getElementById('weather').style.display = 'none';
            } else {
                document.getElementById('error-message').style.display = 'none';
                document.getElementById('weather-city').innerText = city;
                document.getElementById('weather-temperature').innerText = data.temperature;
                document.getElementById('weather-pressure').innerText = data.pressure;
                document.getElementById('weather-humidity').innerText = data.humidity;
                document.getElementById('weather-wind').innerText = data.wind;
                document.getElementById('weather-condition').innerText = data.condition;
                document.getElementById('weather-desc').innerText = data.desc;
                document.getElementById('weather').style.display = 'block';
            }
        })
        .catch(error => {
            document.getElementById('error-message').innerText = 'An error occurred. Please try again.';
            document.getElementById('error-message').style.display = 'block';
            document.getElementById('weather').style.display = 'none';
        });
});
