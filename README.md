# Kafka IoT Sensor Data Pipeline

This project demonstrates a Kafka-based IoT pipeline for streaming, storing, and visualizing sensor data (temperature, humidity). It includes Kafka producers and consumers, PostgreSQL for storage, and Flask for visualization. Additionally, there is an alert system that triggers alerts when sensor readings exceed defined thresholds.

## Table of Contents

- [Kafka IoT Sensor Data Pipeline](#kafka-iot-sensor-data-pipeline)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Architecture](#architecture)
  - [Features](#features)
  - [Technologies](#technologies)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Access the Web UI:](#access-the-web-ui)
    - [Stop the Application:](#stop-the-application)
    - [Clean Up:](#clean-up)
  - [UI Features](#ui-features)
  - [Alerts](#alerts)
  - [Project Structure](#project-structure)
  - [Contributing](#contributing)
  - [License](#license)

## Overview

This project simulates an IoT environment where sensor data is generated and processed in real-time. The data is:
- Produced by a Kafka producer (random sensor data).
- Stored in a PostgreSQL database via a Kafka consumer.
- Visualized through a web UI built with Flask and Plotly.
- An additional alert consumer triggers alerts when sensor readings breach defined thresholds.

## Architecture

- **Kafka Producer**: Simulates IoT devices by generating sensor data and sending it to a Kafka topic (`sensor_data`).
- **Kafka Consumer**: Reads the data from Kafka and stores it in a PostgreSQL database.
- **Alert Consumer**: Monitors the sensor data in real-time and triggers alerts when the temperature or humidity exceeds defined thresholds.
- **PostgreSQL**: Stores sensor data for querying and visualization.
- **Flask Web UI**: Visualizes the sensor data using interactive graphs (temperature and humidity over time).

## Features

- Stream sensor data via Kafka.
- Store sensor data in a PostgreSQL database.
- Visualize real-time sensor data with interactive graphs.
- Trigger alerts for out-of-range sensor readings.

## Technologies

- **Apache Kafka**: Message broker for real-time data streaming.
- **PostgreSQL**: Database for storing sensor data.
- **Flask**: Web framework for building the UI.
- **Plotly**: For interactive graph visualization.
- **Docker**: Containerization platform for managing services.

## Prerequisites

Make sure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/kafka-iot-sensor-data-pipeline.git
   cd kafka-iot-sensor-data-pipeline
   ```

2. Build and run the Docker containers:

   ```bash
   docker-compose up --build
   ```

This command will start the Kafka producer, consumer, alert consumer, PostgreSQL, and the Flask web UI.

## Usage

Once all services are running, you can access the Flask UI to visualize the data and monitor alerts.

### Access the Web UI:

- Open your browser and go to: [http://localhost:5000](http://localhost:5000)

The UI will display real-time interactive graphs of temperature and humidity data.

### Stop the Application:

To stop all running services, use:

```bash
docker-compose down
```

### Clean Up:

To remove containers, volumes, and networks created by Docker Compose, use:

```bash
docker-compose down --volumes
```

## UI Features

- **Temperature Graph**: Displays the temperature sensor data over time.
- **Humidity Graph**: Displays the humidity sensor data over time.

Both graphs are interactive, allowing zooming, panning, and hovering over data points.

## Alerts

The alert consumer monitors the sensor data and triggers alerts when:
- **Temperature** exceeds 30°C (or any predefined threshold).
- **Humidity** exceeds 80% (or any predefined threshold).

To view real-time alerts, check the logs of the `alert_consumer` container:

```bash
docker-compose logs -f alert_consumer
```

Example output when thresholds are breached:

```
alert_consumer_1  | ALERT: High Temperature! Recorded: 35.4°C (Threshold: 30.0°C)
alert_consumer_1  | ALERT: High Humidity! Recorded: 82.0% (Threshold: 80.0%)
```

## Project Structure

```
.
├── producer/              # Kafka producer for generating sensor data
├── consumer/              # Kafka consumer for storing sensor data in PostgreSQL
├── alert_consumer/        # Kafka consumer for triggering alerts
├── ui/                    # Flask app for UI
├── init.sql               # Database setup script for PostgreSQL
├── docker-compose.yml      # Docker Compose configuration
└── README.md              # Project documentation
```

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository, create a new branch, and submit a pull request.

1. Fork the project.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

Licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
