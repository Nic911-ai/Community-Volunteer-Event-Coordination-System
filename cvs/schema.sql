CREATE DATABASE IF NOT EXISTS community_volunteer_system;
USE community_volunteer_system;
-- users: every account (login details + role)
CREATE TABLE users(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(100) NOT NULL, email VARCHAR(120) NOT NULL UNIQUE,
 password_hash VARCHAR(255) NOT NULL, role ENUM('volunteer','organiser','coordinator','supervisor','it') NOT NULL,
 active TINYINT DEFAULT 1, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
-- volunteers: extra profile details for volunteer users
CREATE TABLE volunteers(id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL UNIQUE, phone VARCHAR(30), skills VARCHAR(255),
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id));
-- events: community events created by organisers
CREATE TABLE events(id INT AUTO_INCREMENT PRIMARY KEY, organiser_id INT NOT NULL, supervisor_id INT NULL, title VARCHAR(150) NOT NULL,
 description TEXT, category VARCHAR(50), location VARCHAR(150), event_date DATE NOT NULL, start_time TIME, end_time TIME, capacity INT DEFAULT 0,
 status ENUM('open','closed','cancelled') DEFAULT 'open', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 FOREIGN KEY(organiser_id) REFERENCES users(id), FOREIGN KEY(supervisor_id) REFERENCES users(id));
-- event_registrations: a volunteer signing up for an event (one per volunteer per event)
CREATE TABLE event_registrations(id INT AUTO_INCREMENT PRIMARY KEY, event_id INT NOT NULL, user_id INT NOT NULL,
 status ENUM('pending','approved','rejected','cancelled') DEFAULT 'pending', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 UNIQUE(event_id,user_id), FOREIGN KEY(event_id) REFERENCES events(id), FOREIGN KEY(user_id) REFERENCES users(id));
-- volunteer_availability: weekly time slots a volunteer is free
CREATE TABLE volunteer_availability(id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, day_of_week VARCHAR(10) NOT NULL, start_time TIME NOT NULL, end_time TIME NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id));
-- tasks: jobs inside an event (e.g. Registration Desk)
CREATE TABLE tasks(id INT AUTO_INCREMENT PRIMARY KEY, event_id INT NOT NULL, title VARCHAR(100) NOT NULL, slots INT DEFAULT 1,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY(event_id) REFERENCES events(id));
-- task_assignments: which volunteer does which task
CREATE TABLE task_assignments(id INT AUTO_INCREMENT PRIMARY KEY, task_id INT NOT NULL, user_id INT NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 UNIQUE(task_id,user_id), FOREIGN KEY(task_id) REFERENCES tasks(id), FOREIGN KEY(user_id) REFERENCES users(id));
-- attendance: Present / Absent / Late per volunteer per event
CREATE TABLE attendance(id INT AUTO_INCREMENT PRIMARY KEY, event_id INT NOT NULL, user_id INT NOT NULL, status ENUM('Present','Absent','Late') NOT NULL, recorded_by INT,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
 UNIQUE(event_id,user_id), FOREIGN KEY(event_id) REFERENCES events(id), FOREIGN KEY(user_id) REFERENCES users(id));
-- notifications: in-system messages (no email/SMS)
CREATE TABLE notifications(id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NOT NULL, message VARCHAR(255) NOT NULL, is_read TINYINT DEFAULT 0,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP, FOREIGN KEY(user_id) REFERENCES users(id));
-- activity_logs: audit trail for IT Support
CREATE TABLE activity_logs(id INT AUTO_INCREMENT PRIMARY KEY, user_id INT NULL, action VARCHAR(255) NOT NULL,
 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);
