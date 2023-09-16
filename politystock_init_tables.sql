-- Create the politicians table
CREATE TABLE politicians (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    party VARCHAR(255),
    state VARCHAR(255),
    district VARCHAR(255)
) ENGINE=InnoDB;

-- Create the stocks table
CREATE TABLE stocks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    symbol VARCHAR(10),
    company VARCHAR(255)
) ENGINE=InnoDB;

-- Create the transactions table with foreign key constraints
-- This table may need to wait for the other two tables to actually exist already.
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    politician_id INT,
    stock_id INT,
    transaction_date DATE,
    transaction_type VARCHAR(255),
    amount DECIMAL(10,2),
    FOREIGN KEY (politician_id) REFERENCES politicians(id),
    FOREIGN KEY (stock_id) REFERENCES stocks(id)
) ENGINE=InnoDB;
