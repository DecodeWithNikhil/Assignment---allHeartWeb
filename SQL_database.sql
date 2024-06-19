CREATE DATABASE IF NOT EXISTS web_scraping;

USE web_scraping;

CREATE TABLE websites (
    id INT AUTO_INCREMENT PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    meta_title TEXT,
    meta_description TEXT,
    social_media_links TEXT,
    tech_stack TEXT,
    payment_gateways TEXT,
    language VARCHAR(50)
);
