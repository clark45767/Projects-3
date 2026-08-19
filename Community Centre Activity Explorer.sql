-- =========================================
-- 1. CREATE TABLE
-- =========================================
DROP TABLE IF EXISTS community_activity;

CREATE TABLE community_activity (
    activity_id        INTEGER PRIMARY KEY,
    activity_name       TEXT,
    activity_type        TEXT,
    activity_day         TEXT,
    participant_count    INTEGER,
    duration_minutes     INTEGER
);

-- =========================================
-- 2. INSERT SAMPLE DATA
-- =========================================
INSERT INTO community_activity (activity_name, activity_type, activity_day, participant_count, duration_minutes) VALUES
('Morning Yoga',       'Fitness',    'Monday',    20, 60),
('Book Club',          'Social',     'Monday',    12, 90),
('Basketball League',  'Sports',     'Tuesday',   30, 120),
('Painting Class',     'Arts',       'Tuesday',   15, 75),
('Evening Run',        'Fitness',    'Wednesday', 25, 45),
('Chess Club',         'Social',     'Wednesday', 10, 60),
('Soccer Practice',    'Sports',     'Thursday',  28, 90),
('Pottery Workshop',   'Arts',       'Thursday',  8,  100),
('Zumba Class',        'Fitness',    'Friday',    35, 50),
('Trivia Night',       'Social',     'Friday',    22, 80),
('Volleyball Match',   'Sports',     'Saturday',  24, 100),
('Sketching Class',    'Arts',       'Saturday',  9,  60);

-- =========================================
-- 3. SORT ACTIVITIES (e.g., by participant count, descending)
-- =========================================
SELECT activity_name, activity_type, participant_count
FROM community_activity
ORDER BY participant_count DESC;

-- =========================================
-- 4. SHOW TOP RESULTS (e.g., top 5 most popular activities)
-- =========================================
SELECT activity_name, activity_type, participant_count
FROM community_activity
ORDER BY participant_count DESC
LIMIT 5;

-- =========================================
-- 5. GROUP ACTIVITIES BY TYPE
-- =========================================
SELECT activity_type, COUNT(*) AS number_of_activities
FROM community_activity
GROUP BY activity_type;

-- =========================================
-- 6. CALCULATE TOTALS AND AVERAGES PER TYPE
-- =========================================
SELECT 
    activity_type,
    COUNT(*) AS number_of_activities,
    SUM(participant_count) AS total_participants,
    AVG(duration_minutes) AS avg_duration
FROM community_activity
GROUP BY activity_type;

-- =========================================
-- 7. KEEP ONLY GROUPS MEETING A HAVING CONDITION
--    (e.g., only activity types with more than 50 total participants)
-- =========================================
SELECT 
    activity_type,
    COUNT(*) AS number_of_activities,
    SUM(participant_count) AS total_participants,
    AVG(duration_minutes) AS avg_duration
FROM community_activity
GROUP BY activity_type
HAVING SUM(participant_count) > 50;