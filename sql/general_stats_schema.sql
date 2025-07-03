USE `general_basketball_data`;
-- Create a table for per‐player drive performance
CREATE TABLE IF NOT EXISTS `player_drive_stats` (
  `PLAYER` VARCHAR(100),
  `TEAM` VARCHAR(10),
  `GP` INT,
  `W` INT,
  `L` INT,
  `MIN` INT,
  `DRIVES` INT,
  `FGM` INT,
  `FGA` INT,
  `FG%` DECIMAL(5,2),
  `FTM` INT,
  `FTA` INT,
  `FT%` DECIMAL(5,2),
  `PTS` INT,
  `PTS%` DECIMAL(5,2),
  `PASS` INT,
  `PASS%` DECIMAL(5,2),
  `AST` INT,
  `AST%` DECIMAL(5,2),
  `TO` INT,
  `TOV%` DECIMAL(5,2),
  `PF` INT,
  `PF%` DECIMAL(5,2),
  `Yr` SMALLINT,
  `SeasonType` Varchar(100)
  
) ENGINE=InnoDB
  DEFAULT CHARSET = utf8mb4;
  
USE `general_basketball_data`;
CREATE TABLE shot_distance_ft_data (
    Player VARCHAR(50),
    Team VARCHAR(25),
    Age INTEGER,
    FGM_5less INTEGER,
    FGA_5less INTEGER,
    `FG%_5less` DECIMAL(5,2),
    FGM_5to9 INTEGER,
    FGA_5to9 INTEGER,
    `FG%_5to9` DECIMAL(5,2),
    FGM_10to14 INTEGER,
    FGA_10to14 INTEGER,
    `FG%_10to14` DECIMAL(5,2),
    FGM_15to19 INTEGER,
    FGA_15to19 INTEGER,
    `FG%_15to19` DECIMAL(5,2),
    FGM_20to24 INTEGER,
    FGA_20to24 INTEGER,
    `FG%_20to24` DECIMAL(5,2),
    FGM_25to29 INTEGER,
    FGA_25to29 INTEGER,
    `FG%_25to29` DECIMAL(5,2),
    SeasonType VARCHAR(10),
    Year INTEGER
);

USE `general_basketball_data`;
CREATE TABLE shot_distance_zone_data (
    Player VARCHAR(50),
    Team VARCHAR(25),
    Age INT,
    FGM_RestrictA INT,
    FGA_RestrictA INT,
    `FG%_RestrictA` DECIMAL(5,2),
    FGM_PaintNonRA INT,
    FGA_PaintNonRA INT,
    `FG%_PaintNonRA` DECIMAL(5,2),
    FGM_MidR INT,
    FGA_MidR INT,
    `FG%_MidR` DECIMAL(5,2),
    FGM_LCorn3 INT,
    FGA_LCorn3 INT,
    `FG%_LCorn3` DECIMAL(5,2),
    FGM_RCorn3 INT,
    FGA_RCorn3 INT,
    `FG%_RCorn3` DECIMAL(5,2),
    FGM_Corn3 INT,
    FGA_Corn3 INT,
    `FG%_Corn3` DECIMAL(5,2),
    FGM_AboveBreak3 INT,
    FGA_AboveBreak3 INT,
    `FG%_AboveBreak3` DECIMAL(5,2),
    Year INT, 
    SeasonType VARCHAR(15)
);