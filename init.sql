-- Create the database
CREATE DATABASE IF NOT EXISTS metrics_db;
USE metrics_db;

-- Create tables with indexing for performance
CREATE TABLE talked_time (
                             id INT AUTO_INCREMENT PRIMARY KEY,
                             user_id INT NOT NULL,
                             session_id INT NOT NULL,
                             start_time DATETIME NOT NULL,
                             end_time DATETIME NOT NULL,
                             duration TIME NOT NULL,
                             timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                             INDEX idx_user_session (user_id, session_id)
);

CREATE TABLE microphone_used (
                                 id INT AUTO_INCREMENT PRIMARY KEY,
                                 user_id INT NOT NULL,
                                 session_id INT NOT NULL,
                                 usage_start DATETIME NOT NULL,
                                 usage_end DATETIME NOT NULL,
                                 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                                 INDEX idx_user_session (user_id, session_id)
);

CREATE TABLE speaker_used (
                              id INT AUTO_INCREMENT PRIMARY KEY,
                              user_id INT NOT NULL,
                              session_id INT NOT NULL,
                              usage_start DATETIME NOT NULL,
                              usage_end DATETIME NOT NULL,
                              timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                              INDEX idx_user_session (user_id, session_id)
);

CREATE TABLE voice_sentiment (
                                 id INT AUTO_INCREMENT PRIMARY KEY,
                                 user_id INT NOT NULL,
                                 session_id INT NOT NULL,
                                 sentiment_score DECIMAL(5, 2) NOT NULL,
                                 sentiment_label VARCHAR(50) NOT NULL,
                                 timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
                                 INDEX idx_user_session (user_id, session_id)
);

-- Create stored procedures for inserting data
DELIMITER $$

CREATE PROCEDURE insert_talked_time(
    IN p_user_id INT,
    IN p_session_id INT,
    IN p_start_time DATETIME,
    IN p_end_time DATETIME,
    IN p_duration TIME
)
BEGIN
    INSERT INTO talked_time (user_id, session_id, start_time, end_time, duration)
    VALUES (p_user_id, p_session_id, p_start_time, p_end_time, p_duration);
END$$

CREATE PROCEDURE insert_microphone_used(
    IN p_user_id INT,
    IN p_session_id INT,
    IN p_usage_start DATETIME,
    IN p_usage_end DATETIME
)
BEGIN
    INSERT INTO microphone_used (user_id, session_id, usage_start, usage_end)
    VALUES (p_user_id, p_session_id, p_usage_start, p_usage_end);
END$$

CREATE PROCEDURE insert_speaker_used(
    IN p_user_id INT,
    IN p_session_id INT,
    IN p_usage_start DATETIME,
    IN p_usage_end DATETIME
)
BEGIN
    INSERT INTO speaker_used (user_id, session_id, usage_start, usage_end)
    VALUES (p_user_id, p_session_id, p_usage_start, p_usage_end);
END$$

CREATE PROCEDURE insert_voice_sentiment(
    IN p_user_id INT,
    IN p_session_id INT,
    IN p_sentiment_score DECIMAL(5, 2),
    IN p_sentiment_label VARCHAR(50)
)
BEGIN
    INSERT INTO voice_sentiment (user_id, session_id, sentiment_score, sentiment_label)
    VALUES (p_user_id, p_session_id, p_sentiment_score, p_sentiment_label);
END$$

DELIMITER ;
