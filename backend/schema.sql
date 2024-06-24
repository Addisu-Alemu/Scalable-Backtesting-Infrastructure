-- CREATE TABLE user (
--     id SERIAL PRIMARY KEY,
--     username VARCHAR(50) UNIQUE NOT NULL,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     password_hash VARCHAR(255) NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     last_login TIMESTAMP
-- );
-- CREATE TABLE strategies (
--     strategy_id SERIAL PRIMARY KEY,
--     name VARCHAR(100) NOT NULL,
--     description TEXT,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
-- );
-- CREATE TABLE stocks (
--     stock_id SERIAL PRIMARY KEY,
--     symbol VARCHAR(10) UNIQUE NOT NULL,
--     name VARCHAR(100) NOT NULL,
--     exchange VARCHAR(50)
-- );
-- CREATE TABLE backtests (
--     backtest_id SERIAL PRIMARY KEY,
--     user_id INT,
--     strategy_id INT,
--     stock_id INT,
--     start_date DATE NOT NULL,
--     end_date DATE NOT NULL,
--     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (user_id) REFERENCES users(user_id),
--     FOREIGN KEY (strategy_id) REFERENCES strategies(strategy_id),
--     FOREIGN KEY (stock_id) REFERENCES stocks(stock_id)
-- );
-- CREATE TABLE backtest_results (
--     result_id SERIAL PRIMARY KEY,
--     backtest_id INT,
--     metric_name VARCHAR(50) NOT NULL,
--     metric_value FLOAT NOT NULL,
--     FOREIGN KEY (backtest_id) REFERENCES backtests(backtest_id)
-- );

DROP TABLE IF EXISTS "user";
DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS strategies;
DROP TABLE IF EXISTS stocks;
DROP TABLE IF EXISTS backtests;
DROP TABLE IF EXISTS results;

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255) UNIQUE
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES "user" (id)
);

CREATE TABLE strategies (
    strategy_id SERIAL PRIMARY KEY,
    strategy_name VARCHAR(255),
    description TEXT
);

CREATE TABLE stocks (
    stock_id SERIAL PRIMARY KEY,
    stock_name VARCHAR(255),
    symbol VARCHAR(255)
);

CREATE TABLE scenes (
    scene_id SERIAL PRIMARY KEY,
    start_date DATE,
    end_date DATE
);

CREATE TABLE stock_scenes (
    stock_scene_id SERIAL PRIMARY KEY,
    stock_id INTEGER REFERENCES stocks (stock_id),
    scene_id INTEGER REFERENCES scenes (scene_id)
);

CREATE TABLE strategies_results (
    strategy_result_id SERIAL PRIMARY KEY,
    strategy_id INTEGER REFERENCES strategies (strategy_id),
    stock_scene_id INTEGER REFERENCES stock_scenes (stock_scene_id),
    result REAL
);