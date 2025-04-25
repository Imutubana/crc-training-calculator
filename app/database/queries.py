CREATE_DRIVERS_TABLE = """
CREATE TABLE IF NOT EXISTS drivers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    training_plan TEXT,
    horsepower INTEGER,
    races INTEGER,
    coaching_hours INTEGER
);
"""
