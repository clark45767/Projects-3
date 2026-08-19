-- =========================================
-- 1. CREATE TABLE
-- =========================================
DROP TABLE IF EXISTS observations;

CREATE TABLE observations (
    observation_id   INTEGER PRIMARY KEY,
    animal_group      TEXT,
    habitat           TEXT,
    estimated_weight  REAL,   -- in kg
    observation_depth REAL    -- in metres
);

-- =========================================
-- 2. INSERT SAMPLE DATA
-- =========================================
INSERT INTO observations (animal_group, habitat, estimated_weight, observation_depth) VALUES
('Shark',   'Coral Reef', 150.5, 12.0),
('Turtle',  'Coral Reef', 45.2,  8.5),
('Shark',   'Open Ocean', 200.0, 30.0),
('Dolphin', 'Open Ocean', 180.3, 15.0),
('Turtle',  'Seagrass',   40.1,  5.0),
('Ray',     'Coral Reef', 60.0,  10.0),
('Dolphin', 'Open Ocean', 175.0, 20.0),
('Ray',     'Seagrass',   55.5,  6.0),
('Shark',   'Coral Reef', 160.0, 14.0),
('Turtle',  'Open Ocean', 42.0,  25.0);

-- =========================================
-- 3. SELECT DISTINCT — show each animal group once
-- =========================================
SELECT DISTINCT animal_group
FROM observations;

-- =========================================
-- 4. COUNT() — count all observations
-- =========================================
SELECT COUNT(*) AS total_observations
FROM observations;

-- =========================================
-- 5. COUNT() — observations from a selected habitat
-- =========================================
SELECT COUNT(*) AS reef_observations
FROM observations
WHERE habitat = 'Coral Reef';

-- =========================================
-- 6. SUM() — total estimated weight
-- =========================================
SELECT SUM(estimated_weight) AS total_weight
FROM observations;

-- =========================================
-- 7. AVG() — average observation depth
-- =========================================
SELECT AVG(observation_depth) AS avg_depth
FROM observations;

-- =========================================
-- 8. COMBINE multiple aggregate functions
-- =========================================
SELECT 
    COUNT(*) AS total_observations,
    SUM(estimated_weight) AS total_weight,
    AVG(observation_depth) AS avg_depth
FROM observations;