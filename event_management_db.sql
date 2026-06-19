USE event_management_db;

SET FOREIGN_KEY_CHECKS = 0;
SET autocommit = 1;

DROP TABLE IF EXISTS audit_logs;
DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS registrations;
DROP TABLE IF EXISTS events;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS refresh_tokens;
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS roles;

SET FOREIGN_KEY_CHECKS = 1;

-- =====================
-- ROLES
-- =====================
CREATE TABLE roles (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO roles (id, name) VALUES (1, 'Admin');
INSERT INTO roles (id, name) VALUES (2, 'Organizer');
INSERT INTO roles (id, name) VALUES (3, 'Participant');

-- =====================
-- USERS
-- =====================
CREATE TABLE users (
    id INT PRIMARY KEY AUTO_INCREMENT,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role_id INT NOT NULL DEFAULT 3,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_users_role FOREIGN KEY (role_id) REFERENCES roles(id)
);

-- =====================
-- CATEGORIES
-- =====================
CREATE TABLE categories (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================
-- EVENTS
-- =====================
CREATE TABLE events (
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    venue VARCHAR(255) NOT NULL,
    capacity INT NOT NULL,
    category_id INT,
    organizer_id INT NOT NULL,
    status ENUM('Upcoming','Ongoing','Completed','Cancelled') DEFAULT 'Upcoming',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_events_category FOREIGN KEY (category_id) REFERENCES categories(id),
    CONSTRAINT fk_events_organizer FOREIGN KEY (organizer_id) REFERENCES users(id)
);

-- =====================
-- REGISTRATIONS
-- =====================
CREATE TABLE registrations (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    event_id INT NOT NULL,
    status ENUM('Registered','Cancelled') DEFAULT 'Registered',
    registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_registration UNIQUE (user_id, event_id),
    CONSTRAINT fk_reg_user FOREIGN KEY (user_id) REFERENCES users(id),
    CONSTRAINT fk_reg_event FOREIGN KEY (event_id) REFERENCES events(id)
);

-- =====================
-- TICKETS
-- =====================
CREATE TABLE tickets (
    id INT PRIMARY KEY AUTO_INCREMENT,
    registration_id INT NOT NULL,
    ticket_number VARCHAR(100) UNIQUE NOT NULL,
    status ENUM('Active','Used','Cancelled') DEFAULT 'Active',
    issued_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_ticket_registration FOREIGN KEY (registration_id) REFERENCES registrations(id)
);

-- =====================
-- ATTENDANCE
-- =====================
CREATE TABLE attendance (
    id INT PRIMARY KEY AUTO_INCREMENT,
    event_id INT NOT NULL,
    user_id INT NOT NULL,
    status VARCHAR(50) DEFAULT 'Present',
    attendance_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_attendance_event FOREIGN KEY (event_id) REFERENCES events(id),
    CONSTRAINT fk_attendance_user FOREIGN KEY (user_id) REFERENCES users(id)
);

-- =====================
-- REFRESH TOKENS
-- =====================
CREATE TABLE refresh_tokens (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT NOT NULL,
    token TEXT NOT NULL,
    expires_at DATETIME NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_refresh_user FOREIGN KEY (user_id) REFERENCES users(id)
);

-- =====================
-- AUDIT LOGS
-- =====================
CREATE TABLE audit_logs (
    id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    action VARCHAR(255) NOT NULL,
    entity_type VARCHAR(100),
    entity_id INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_audit_user FOREIGN KEY (user_id) REFERENCES users(id)
);

-- =====================
-- VERIFY
-- =====================
SELECT * FROM users;
SET SQL_SAFE_UPDATES = 0;
UPDATE users SET role_id = 1 WHERE id = 1;
COMMIT;
SELECT id, email, role_id FROM users;