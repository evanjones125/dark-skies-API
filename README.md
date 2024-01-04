# Dark Skies API

## Introduction
Welcome! The Dark Skies API is a free, read-only API that returns JSON-formatted astronomy data. Right now, there's a singular endpoint that will return the following output for any date/location combo:
- Milky Way visibility data
- Sunrise and sunset times
- "Dark windows" for nighttime star viewing in which neither the sun nor the moon are above the horizon (both of these celestial bodies have a tendency to obscure the stars and galaxies that would otherwise be visible)

I made this as part of a larger project because I couldn't find a free Milky Way API. The above source code gives you everything you need to set up your own API endpoint if you want to do that.

## Usage
You can directly use the Dark Skies API at `https://roadtrip-dashboard-backend.vercel.app/api/astronomy/astronomyForecast/{lat},{lon},{date}/`. Replace `{lat}`, `{lon}`, and `{date}` with your desired latitude, longitude, and date in `YYYY-MM-DD` format.

#### Example API payload for .../37.67000,-112.16000,2024-04-13/:
```
{
    "milkyWay": {
        "visibility": {"start": "1:15am", "end": "5:23am"},
        "position": "Arch (10deg) - Arch (55deg)",
        "report": "The milky way will be visible for a 4 hour, 8 minute window between 1:15am and 5:23am. The galactic center will be visible in the same window. This will be one of the best nights to view the milky way in 2024!",
    },
    "sunAndMoon": {
        "sunrise": "6:55am",
        "sunset": "8:03pm",
        "darkWindows": [["2:10am", "6:54am"]],
    },
}
```

## Local Setup and Installation
If you prefer to run the API locally or you want to contribute to the Dark Skies API, here's how you can do that:

1. Clone this repo to your local machine:
```
git clone https://github.com/evanjones125/dark-skies-API.git
```
2. Get an IPGeolocation API Key and paste it in on line 9 of main.py. The Dark Skies API relies, in part, on an external call to the IPGeolocation API. You can get a free API key from them <a href="https://app.ipgeolocation.io/signup">here</a> (the free tier allows you to make up to 1,000 requests per day).
3. Run the [main.py](src/main.py) script, passing in your latitude, longitude, and date as arguments to the fetch_astronomy_data function.

Please feel free as well to set up your own API endpoint based on this source code if you want different functionality or need more capacity.

## Dependencies
This project relies on standard Python libraries. There are no external dependencies required.

## Example implementation
I call this API in the backend of a <a href="">road trip dashboard project</a> that I made to display astronomy data for all the dates associated with a location along a road trip.

<img src="https://raw.githubusercontent.com/evanjones125/road-trip-dashboard/main/frontend/src/assets/screenshot_detailed.png" height="300px">

## Future features
In the near future, I'm planning on adding milky way data beyond just the American Southwest (note: the dark windows feature will work for any location in the world but the Milky Way data you get will be for Southern Utah).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Milky Way visibility data provided by <a href="https://capturetheatlas.com/how-to-photograph-the-milky-way/">Capture The Atlas</a>
- Sun and moon data powered by the IPGeolocation API