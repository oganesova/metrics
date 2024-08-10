import mysql.connector
from mysql.connector import Error
from flask import Flask, request, jsonify
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

DB_CONFIG = {
    'host': 'db',
    'user': 'root',
    'password': '1111',
    'database': 'metrics_db'
}


def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            logging.info("Successfully connected to the database.")
            return connection
    except Error as e:
        logging.error(f"Error connecting to MySQL: {e}")
    return None


@app.route('/metrics/talked_time', methods=['POST'])
def insert_talked_time():
    data = request.json
    logging.debug(f"Received data for talked_time: {data}")

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "CALL insert_talked_time(%s, %s, %s, %s, %s)"
        values = (data['user_id'], data['session_id'], data['start_time'], data['end_time'], data['duration'])
        logging.debug(f"Executing query: {query} with values: {values}")

        try:
            cursor.execute(query, values)
            connection.commit()
            logging.info("Data inserted successfully into talked_time.")
            return jsonify({"message": "Data inserted successfully into talked_time"}), 201
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return jsonify({"error": str(e)}), 400
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Failed to connect to the database"}), 500


@app.route('/metrics/microphone_used', methods=['POST'])
def insert_microphone_used():
    data = request.json
    logging.debug(f"Received data for microphone_used: {data}")

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "CALL insert_microphone_used(%s, %s, %s, %s)"
        values = (data['user_id'], data['session_id'], data['usage_start'], data['usage_end'])
        logging.debug(f"Executing query: {query} with values: {values}")

        try:
            cursor.execute(query, values)
            connection.commit()
            logging.info("Data inserted successfully into microphone_used.")
            return jsonify({"message": "Data inserted successfully into microphone_used"}), 201
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return jsonify({"error": str(e)}), 400
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Failed to connect to the database"}), 500


@app.route('/metrics/speaker_used', methods=['POST'])
def insert_speaker_used():
    data = request.json
    logging.debug(f"Received data for speaker_used: {data}")

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "CALL insert_speaker_used(%s, %s, %s, %s)"
        values = (data['user_id'], data['session_id'], data['usage_start'], data['usage_end'])
        logging.debug(f"Executing query: {query} with values: {values}")

        try:
            cursor.execute(query, values)
            connection.commit()
            logging.info("Data inserted successfully into speaker_used.")
            return jsonify({"message": "Data inserted successfully into speaker_used"}), 201
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return jsonify({"error": str(e)}), 400
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Failed to connect to the database"}), 500


@app.route('/metrics/speaker_used', methods=['GET'])
def get_speaker_used():
    logging.debug("Received request to get speaker_used data.")

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor(dictionary=True)  # Use dictionary=True to get results as dictionaries
        query = "SELECT * FROM speaker_used"
        logging.debug(f"Executing query: {query}")

        try:
            cursor.execute(query)
            results = cursor.fetchall()
            logging.info("Data retrieved successfully from speaker_used.")
            return jsonify(results), 200
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return jsonify({"error": str(e)}), 400
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Failed to connect to the database"}), 500


@app.route('/metrics/voice_sentiment', methods=['POST'])
def insert_voice_sentiment():
    """Handle POST requests to insert data into the voice_sentiment table."""
    data = request.json
    logging.debug(f"Received data for voice_sentiment: {data}")

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = "CALL insert_voice_sentiment(%s, %s, %s, %s)"
        values = (data['user_id'], data['session_id'], data['sentiment_score'], data['sentiment_label'])
        logging.debug(f"Executing query: {query} with values: {values}")

        try:
            cursor.execute(query, values)
            connection.commit()
            logging.info("Data inserted successfully into voice_sentiment.")
            return jsonify({"message": "Data inserted successfully into voice_sentiment"}), 201
        except Error as e:
            logging.error(f"Error executing query: {e}")
            return jsonify({"error": str(e)}), 400
        finally:
            cursor.close()
            connection.close()
    return jsonify({"error": "Failed to connect to the database"}), 500


if __name__ == '__main__':
    app.run(debug=True)
