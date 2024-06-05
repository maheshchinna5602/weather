document.addEventListener('DOMContentLoaded', () => {
    fetch('/weather')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            displayWeather(data);
        })
        .catch(error => {
            console.error('There was a problem fetching the weather data:', error);
        });

    function displayWeather(data) {
        console.log(data)
        const cityElement = document.querySelector('.city');
        const temperatureElement = document.querySelector('.temperature');
        const descriptionElement = document.querySelector('.description');

        cityElement.textContent = data.city;
        temperatureElement.textContent = `35 °C`;
        descriptionElement.textContent = data.description;
    }
});
