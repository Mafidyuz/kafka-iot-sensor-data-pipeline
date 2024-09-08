-- Create the user only if it doesn't exist
DO
$$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE rolname = 'userkafka') THEN
      CREATE USER "userkafka" WITH PASSWORD 'password';
   END IF;
END
$$;

-- Grant privileges on the sensor_data database to userkafka
GRANT ALL PRIVILEGES ON DATABASE sensor_data TO "userkafka";

\connect sensor_data;

-- Create the sensor_data table if it doesn't exist
CREATE TABLE IF NOT EXISTS sensor_data (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature DECIMAL,
    humidity DECIMAL
);
