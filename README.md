# Garbage Collection Schedule ICS Generator

## Overview

This project generates an `.ics` file containing the garbage collection schedule for a specific address serviced by IVAREM in Mechelen. The `.ics` file can be imported into any calendar application to keep track of garbage collection days. The application uses an API to retrieve garbage collection data and converts it into a calendar format using the `ical` library.

## Features

- Retrieves garbage collection data via an API.
- Converts the data into a calendar format and generates an `.ics` file.
- Compatible with most calendar applications, such as Google Calendar, Outlook, and Apple Calendar.

## How to Use

1. **Clone the Repository**  

Clone this repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

2. **Set Up Environment Variables**

Create a .env file in the root directory with the following structure:

```plaintext
API_TOKEN=<your-api-token>
ADDRESS=<specific-address>
```

Replace <your-api-token> with the token required for accessing the API.
Replace <specific-address> with the address for which you want to fetch the garbage collection schedule.

3. **Install Dependencies**

Install the required Python packages:

```bash
pip install -r requirements.txt
```

4. **Run the Application**

Execute the script to generate the .ics file:

```bash
python generate_calendar.py
```

The generated file will be saved in the project directory as *calendar.ics*.

5. **Import the .ics File into Your Calendar**

Open your preferred calendar application.
Import the calendar.ics file to view the garbage collection schedule.

## Limitations

### API Token Refresh

The API token must be periodically refreshed to ensure continued access.
You will need to update the API_TOKEN value in the .env file whenever the token expires.


## Address Limitation

The application currently supports only a single address specified in the .env file.
Extending the functionality to support multiple addresses would require additional development.

## Dependency on API Availability

The application relies on the availability and reliability of the external API. If the API changes or becomes unavailable, the application may not function correctly.

## Future Improvements
- Add support for multiple addresses.
- Implement automatic token refresh.
- Provide a graphical user interface (GUI) for easier use.

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request for bug fixes, new features, or improvements.

## License
This project is licensed under the MIT License.

## Acknowledgments
Thanks to IVAREM for providing the garbage collection schedule data.
The ical library for facilitating calendar creation.