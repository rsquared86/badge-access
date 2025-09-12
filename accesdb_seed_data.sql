select * from AccessPoints ap ;
select * from Buildings b ;
select * from Check_in ci ;
select * from Person p ;
select * from PersonRoles pr ;
select * from Roles r ;



-- Insert Roles
INSERT INTO Roles (role_name) VALUES 
    ('Student'),
    ('Faculty'),
    ('Staff'),
    ('Administrator'),
    ('Visitor'),
    ('Graduate Student'),
    ('Research Assistant'),
    ('Security'),
    ('Maintenance'),
    ('Contractor');

-- Insert Buildings
INSERT INTO Buildings (name) VALUES 
    ('Academic Hall'),
    ('Science Center'),
    ('Library'),
    ('Student Union'),
    ('Engineering Building'),
    ('Arts & Humanities'),
    ('Business School'),
    ('Dormitory A'),
    ('Dormitory B'),
    ('Dormitory C'),
    ('Cafeteria'),
    ('Gymnasium'),
    ('Medical Center'),
    ('Administration Building'),
    ('Parking Garage');

-- Insert Access Points for each building
INSERT INTO AccessPoints (building_id, ap_id, ap_name, type) VALUES 
    -- Academic Hall (building_id: 1)
    (1, 1, 'Main Entrance', 'Door'),
    (1, 2, 'Side Entrance', 'Door'),
    (1, 3, 'Emergency Exit', 'Emergency'),
    
    -- Science Center (building_id: 2)
    (2, 1, 'Main Lobby', 'Door'),
    (2, 2, 'Lab Wing Entrance', 'Door'),
    (2, 3, 'Research Wing', 'Secure Door'),
    (2, 4, 'Service Entrance', 'Door'),
    
    -- Library (building_id: 3)
    (3, 1, 'Main Entrance', 'Turnstile'),
    (3, 2, 'Staff Entrance', 'Door'),
    (3, 3, 'Study Room Access', 'Door'),
    
    -- Student Union (building_id: 4)
    (4, 1, 'Main Entrance', 'Door'),
    (4, 2, 'Food Court Entrance', 'Door'),
    (4, 3, 'Event Hall', 'Door'),
    
    -- Engineering Building (building_id: 5)
    (5, 1, 'Main Entrance', 'Door'),
    (5, 2, 'Workshop Entrance', 'Secure Door'),
    (5, 3, 'Computer Lab', 'Secure Door'),
    
    -- Arts & Humanities (building_id: 6)
    (6, 1, 'Main Entrance', 'Door'),
    (6, 2, 'Theater Entrance', 'Door'),
    
    -- Business School (building_id: 7)
    (7, 1, 'Main Entrance', 'Door'),
    (7, 2, 'Executive Entrance', 'Secure Door'),
    
    -- Dormitory A (building_id: 8)
    (8, 1, 'Main Entrance', 'Secure Door'),
    (8, 2, 'Side Entrance', 'Secure Door'),
    
    -- Dormitory B (building_id: 9)
    (9, 1, 'Main Entrance', 'Secure Door'),
    (9, 2, 'Courtyard Entrance', 'Secure Door'),
    
    -- Dormitory C (building_id: 10)
    (10, 1, 'Main Entrance', 'Secure Door'),
    (10, 2, 'Garden Entrance', 'Secure Door'),
    
    -- Cafeteria (building_id: 11)
    (11, 1, 'Main Entrance', 'Door'),
    (11, 2, 'Kitchen Staff', 'Secure Door'),
    
    -- Gymnasium (building_id: 12)
    (12, 1, 'Main Entrance', 'Door'),
    (12, 2, 'Equipment Room', 'Secure Door'),
    
    -- Medical Center (building_id: 13)
    (13, 1, 'Main Entrance', 'Door'),
    (13, 2, 'Emergency Entrance', 'Door'),
    (13, 3, 'Staff Only', 'Secure Door'),
    
    -- Administration Building (building_id: 14)
    (14, 1, 'Main Entrance', 'Door'),
    (14, 2, 'Executive Wing', 'Secure Door'),
    
    -- Parking Garage (building_id: 15)
    (15, 1, 'Vehicle Entrance', 'Gate'),
    (15, 2, 'Pedestrian Entrance', 'Door');

    
-- Insert 100+ Student Records and other personnel
INSERT INTO Person (card_uid, first_name, last_name, email) VALUES 
    -- Students (IDs: 1-120)
    ('1001234567', 'Emma', 'Johnson', 'emma.johnson@ucdenver.edu'),
    ('1001234568', 'Liam', 'Williams', 'liam.williams@ucdenver.edu'),
    ('1001234569', 'Olivia', 'Brown', 'olivia.brown@ucdenver.edu'),
    ('1001234570', 'Noah', 'Jones', 'noah.jones@ucdenver.edu'),
    ('1001234571', 'Ava', 'Garcia', 'ava.garcia@ucdenver.edu'),
    ('1001234572', 'Elijah', 'Miller', 'elijah.miller@ucdenver.edu'),
    ('1001234573', 'Sophia', 'Davis', 'sophia.davis@ucdenver.edu'),
    ('1001234574', 'Lucas', 'Rodriguez', 'lucas.rodriguez@ucdenver.edu'),
    ('1001234575', 'Isabella', 'Wilson', 'isabella.wilson@ucdenver.edu'),
    ('1001234576', 'Mason', 'Martinez', 'mason.martinez@ucdenver.edu'),
    ('1001234577', 'Mia', 'Anderson', 'mia.anderson@ucdenver.edu'),
    ('1001234578', 'Ethan', 'Taylor', 'ethan.taylor@ucdenver.edu'),
    ('1001234579', 'Charlotte', 'Thomas', 'charlotte.thomas@ucdenver.edu'),
    ('1001234580', 'Alexander', 'Hernandez', 'alexander.hernandez@ucdenver.edu'),
    ('1001234581', 'Amelia', 'Moore', 'amelia.moore@ucdenver.edu'),
    ('1001234582', 'Daniel', 'Martin', 'daniel.martin@ucdenver.edu'),
    ('1001234583', 'Harper', 'Jackson', 'harper.jackson@ucdenver.edu'),
    ('1001234584', 'Matthew', 'Thompson', 'matthew.thompson@ucdenver.edu'),
    ('1001234585', 'Evelyn', 'White', 'evelyn.white@ucdenver.edu'),
    ('1001234586', 'Henry', 'Lopez', 'henry.lopez@ucdenver.edu'),
    ('1001234587', 'Abigail', 'Lee', 'abigail.lee@ucdenver.edu'),
    ('1001234588', 'Jackson', 'Gonzalez', 'jackson.gonzalez@ucdenver.edu'),
    ('1001234589', 'Emily', 'Harris', 'emily.harris@ucdenver.edu'),
    ('1001234590', 'Sebastian', 'Clark', 'sebastian.clark@ucdenver.edu'),
    ('1001234591', 'Elizabeth', 'Lewis', 'elizabeth.lewis@ucdenver.edu'),
    ('1001234592', 'Aiden', 'Robinson', 'aiden.robinson@ucdenver.edu'),
    ('1001234593', 'Sofia', 'Walker', 'sofia.walker@ucdenver.edu'),
    ('1001234594', 'David', 'Perez', 'david.perez@ucdenver.edu'),
    ('1001234595', 'Avery', 'Hall', 'avery.hall@ucdenver.edu'),
    ('1001234596', 'Joseph', 'Young', 'joseph.young@ucdenver.edu'),
    ('1001234597', 'Scarlett', 'Allen', 'scarlett.allen@ucdenver.edu'),
    ('1001234598', 'Samuel', 'Sanchez', 'samuel.sanchez@ucdenver.edu'),
    ('1001234599', 'Victoria', 'Wright', 'victoria.wright@ucdenver.edu'),
    ('1001234600', 'Benjamin', 'King', 'benjamin.king@ucdenver.edu'),
    ('1001234601', 'Madison', 'Scott', 'madison.scott@ucdenver.edu'),
    ('1001234602', 'Christopher', 'Green', 'christopher.green@ucdenver.edu'),
    ('1001234603', 'Luna', 'Baker', 'luna.baker@ucdenver.edu'),
    ('1001234604', 'Andrew', 'Adams', 'andrew.adams@ucdenver.edu'),
    ('1001234605', 'Grace', 'Nelson', 'grace.nelson@ucdenver.edu'),
    ('1001234606', 'Joshua', 'Hill', 'joshua.hill@ucdenver.edu'),
    ('1001234607', 'Chloe', 'Ramirez', 'chloe.ramirez@ucdenver.edu'),
    ('1001234608', 'John', 'Campbell', 'john.campbell@ucdenver.edu'),
    ('1001234609', 'Penelope', 'Mitchell', 'penelope.mitchell@ucdenver.edu'),
    ('1001234610', 'Ryan', 'Roberts', 'ryan.roberts@ucdenver.edu'),
    ('1001234611', 'Layla', 'Carter', 'layla.carter@ucdenver.edu'),
    ('1001234612', 'Jaxon', 'Phillips', 'jaxon.phillips@ucdenver.edu'),
    ('1001234613', 'Riley', 'Evans', 'riley.evans@ucdenver.edu'),
    ('1001234614', 'Luke', 'Turner', 'luke.turner@ucdenver.edu'),
    ('1001234615', 'Zoey', 'Torres', 'zoey.torres@ucdenver.edu'),
    ('1001234616', 'Anthony', 'Parker', 'anthony.parker@ucdenver.edu'),
    ('1001234617', 'Nora', 'Collins', 'nora.collins@ucdenver.edu'),
    ('1001234618', 'Isaac', 'Edwards', 'isaac.edwards@ucdenver.edu'),
    ('1001234619', 'Lily', 'Stewart', 'lily.stewart@ucdenver.edu'),
    ('1001234620', 'Aaron', 'Flores', 'aaron.flores@ucdenver.edu'),
    ('1001234621', 'Eleanor', 'Morris', 'eleanor.morris@ucdenver.edu'),
    ('1001234622', 'Jordan', 'Nguyen', 'jordan.nguyen@ucdenver.edu'),
    ('1001234623', 'Hannah', 'Murphy', 'hannah.murphy@ucdenver.edu'),
    ('1001234624', 'Cooper', 'Rivera', 'cooper.rivera@ucdenver.edu'),
    ('1001234625', 'Lillian', 'Cook', 'lillian.cook@ucdenver.edu'),
    ('1001234626', 'Evan', 'Rogers', 'evan.rogers@ucdenver.edu'),
    ('1001234627', 'Addison', 'Morgan', 'addison.morgan@ucdenver.edu'),
    ('1001234628', 'Christian', 'Peterson', 'christian.peterson@ucdenver.edu'),
    ('1001234629', 'Aubrey', 'Cooper', 'aubrey.cooper@ucdenver.edu'),
    ('1001234630', 'Maverick', 'Reed', 'maverick.reed@ucdenver.edu'),
    ('1001234631', 'Savannah', 'Bailey', 'savannah.bailey@ucdenver.edu'),
    ('1001234632', 'Greyson', 'Bell', 'greyson.bell@ucdenver.edu'),
    ('1001234633', 'Brooklyn', 'Gomez', 'brooklyn.gomez@ucdenver.edu'),
    ('1001234634', 'Jonathan', 'Kelly', 'jonathan.kelly@ucdenver.edu'),
    ('1001234635', 'Leah', 'Howard', 'leah.howard@ucdenver.edu'),
    ('1001234636', 'Tyler', 'Ward', 'tyler.ward@ucdenver.edu'),
    ('1001234637', 'Zoe', 'Cox', 'zoe.cox@ucdenver.edu'),
    ('1001234638', 'Nathan', 'Diaz', 'nathan.diaz@ucdenver.edu'),
    ('1001234639', 'Audrey', 'Richardson', 'audrey.richardson@ucdenver.edu'),
    ('1001234640', 'Caleb', 'Wood', 'caleb.wood@ucdenver.edu'),
    ('1001234641', 'Maya', 'Watson', 'maya.watson@ucdenver.edu'),
    ('1001234642', 'Ryan', 'Brooks', 'ryan.brooks@ucdenver.edu'),
    ('1001234643', 'Genesis', 'Bennett', 'genesis.bennett@ucdenver.edu'),
    ('1001234644', 'Nicholas', 'Gray', 'nicholas.gray@ucdenver.edu'),
    ('1001234645', 'Aaliyah', 'James', 'aaliyah.james@ucdenver.edu'),
    ('1001234646', 'Ian', 'Reyes', 'ian.reyes@ucdenver.edu'),
    ('1001234647', 'Kennedy', 'Cruz', 'kennedy.cruz@ucdenver.edu'),
    ('1001234648', 'Jeremiah', 'Hughes', 'jeremiah.hughes@ucdenver.edu'),
    ('1001234649', 'Kinsley', 'Price', 'kinsley.price@ucdenver.edu'),
    ('1001234650', 'Gavin', 'Myers', 'gavin.myers@ucdenver.edu'),
    ('1001234651', 'Allison', 'Long', 'allison.long@ucdenver.edu'),
    ('1001234652', 'Connor', 'Foster', 'connor.foster@ucdenver.edu'),
    ('1001234653', 'Naomi', 'Sanders', 'naomi.sanders@ucdenver.edu'),
    ('1001234654', 'Cameron', 'Ross', 'cameron.ross@ucdenver.edu'),
    ('1001234655', 'Violet', 'Morales', 'violet.morales@ucdenver.edu'),
    ('1001234656', 'Juan', 'Powell', 'juan.powell@ucdenver.edu'),
    ('1001234657', 'Stella', 'Sullivan', 'stella.sullivan@ucdenver.edu'),
    ('1001234658', 'Hunter', 'Russell', 'hunter.russell@ucdenver.edu'),
    ('1001234659', 'Claire', 'Ortiz', 'claire.ortiz@ucdenver.edu'),
    ('1001234660', 'Eli', 'Jenkins', 'eli.jenkins@ucdenver.edu'),
    ('1001234661', 'Bella', 'Gutierrez', 'bella.gutierrez@ucdenver.edu'),
    ('1001234662', 'Landon', 'Perry', 'landon.perry@ucdenver.edu'),
    ('1001234663', 'Skylar', 'Butler', 'skylar.butler@ucdenver.edu'),
    ('1001234664', 'Colton', 'Barnes', 'colton.barnes@ucdenver.edu'),
    ('1001234665', 'Lucy', 'Fisher', 'lucy.fisher@ucdenver.edu'),
    ('1001234666', 'Brayden', 'Henderson', 'brayden.henderson@ucdenver.edu'),
    ('1001234667', 'Paisley', 'Coleman', 'paisley.coleman@ucdenver.edu'),
    ('1001234668', 'Adam', 'Simmons', 'adam.simmons@ucdenver.edu'),
    ('1001234669', 'Samantha', 'Patterson', 'samantha.patterson@ucdenver.edu'),
    ('1001234670', 'Xavier', 'Jordan', 'xavier.jordan@ucdenver.edu'),
    ('1001234671', 'Caroline', 'Reynolds', 'caroline.reynolds@ucdenver.edu'),
    ('1001234672', 'Thomas', 'Hamilton', 'thomas.hamilton@ucdenver.edu'),
    ('1001234673', 'Anna', 'Graham', 'anna.graham@ucdenver.edu'),
    ('1001234674', 'Ayden', 'Kim', 'ayden.kim@ucdenver.edu'),
    ('1001234675', 'Genesis', 'Butler', 'genesis.butler2@ucdenver.edu'),
    ('1001234676', 'Angel', 'Simmons', 'angel.simmons@ucdenver.edu'),
    ('1001234677', 'Sarah', 'Foster', 'sarah.foster@ucdenver.edu'),
    ('1001234678', 'Robert', 'Bryant', 'robert.bryant@ucdenver.edu'),
    ('1001234679', 'Madelyn', 'Alexander', 'madelyn.alexander@ucdenver.edu'),
    ('1001234680', 'Antonio', 'Griffin', 'antonio.griffin@ucdenver.edu'),
    ('1001234681', 'Brooklyn', 'Diaz', 'brooklyn.diaz2@ucdenver.edu'),
    ('1001234682', 'Jose', 'Hayes', 'jose.hayes@ucdenver.edu'),
    ('1001234683', 'Jasmine', 'Myers', 'jasmine.myers@ucdenver.edu'),
    ('1001234684', 'Kevin', 'Ford', 'kevin.ford@ucdenver.edu'),
    ('1001234685', 'Delilah', 'Hamilton', 'delilah.hamilton@ucdenver.edu'),
    ('1001234686', 'Louis', 'Graham', 'louis.graham@ucdenver.edu'),

    -- Faculty (IDs: 121-140)
    ('2001000001', 'Dr. James', 'Peterson', 'j.peterson@ucdenver.edu'),
    ('2001000002', 'Dr. Mary', 'Thompson', 'm.thompson@ucdenver.edu'),
    ('2001000003', 'Dr. Robert', 'Anderson', 'r.anderson@ucdenver.edu'),
    ('2001000004', 'Dr. Linda', 'Wilson', 'l.wilson@ucdenver.edu'),
    ('2001000005', 'Dr. Michael', 'Davis', 'm.davis@ucdenver.edu'),
    ('2001000006', 'Dr. Patricia', 'Miller', 'p.miller@ucdenver.edu'),
    ('2001000007', 'Dr. William', 'Moore', 'w.moore@ucdenver.edu'),
    ('2001000008', 'Dr. Elizabeth', 'Taylor', 'e.taylor@ucdenver.edu'),
    ('2001000009', 'Dr. David', 'Brown', 'd.brown@ucdenver.edu'),
    ('2001000010', 'Dr. Barbara', 'Johnson', 'b.johnson@ucdenver.edu'),
    ('2001000011', 'Dr. Richard', 'Jones', 'r.jones@ucdenver.edu'),
    ('2001000012', 'Dr. Susan', 'Garcia', 's.garcia@ucdenver.edu'),
    ('2001000013', 'Dr. Joseph', 'Rodriguez', 'j.rodriguez@ucdenver.edu'),
    ('2001000014', 'Dr. Jessica', 'Martinez', 'j.martinez@ucdenver.edu'),
    ('2001000015', 'Dr. Thomas', 'Hernandez', 't.hernandez@ucdenver.edu'),
    ('2001000016', 'Dr. Sarah', 'Lopez', 's.lopez@ucdenver.edu'),
    ('2001000017', 'Dr. Charles', 'Gonzalez', 'c.gonzalez@ucdenver.edu'),
    ('2001000018', 'Dr. Karen', 'Wilson', 'k.wilson2@ucdenver.edu'),
    ('2001000019', 'Dr. Daniel', 'Anderson', 'd.anderson2@ucdenver.edu'),
    ('2001000020', 'Dr. Nancy', 'Thomas', 'n.thomas@ucdenver.edu'),

    -- Staff (IDs: 141-160)
    ('3001000001', 'John', 'Smith', 'j.smith@ucdenver.edu'),
    ('3001000002', 'Jennifer', 'Brown', 'j.brown@ucdenver.edu'),
    ('3001000003', 'Michael', 'Johnson', 'm.johnson@ucdenver.edu'),
    ('3001000004', 'Lisa', 'Williams', 'l.williams@ucdenver.edu'),
    ('3001000005', 'Christopher', 'Jones', 'c.jones@ucdenver.edu'),
    ('3001000006', 'Amanda', 'Garcia', 'a.garcia@ucdenver.edu'),
    ('3001000007', 'Matthew', 'Miller', 'm.miller@ucdenver.edu'),
    ('3001000008', 'Ashley', 'Davis', 'a.davis@ucdenver.edu'),
    ('3001000009', 'David', 'Rodriguez', 'd.rodriguez@ucdenver.edu'),
    ('3001000010', 'Jessica', 'Wilson', 'j.wilson@ucdenver.edu'),
    ('3001000011', 'Andrew', 'Martinez', 'a.martinez@ucdenver.edu'),
    ('3001000012', 'Sarah', 'Anderson', 's.anderson@ucdenver.edu'),
    ('3001000013', 'Daniel', 'Taylor', 'd.taylor@ucdenver.edu'),
    ('3001000014', 'Stephanie', 'Thomas', 's.thomas@ucdenver.edu'),
    ('3001000015', 'Ryan', 'Hernandez', 'r.hernandez@ucdenver.edu'),
    ('3001000016', 'Michelle', 'Moore', 'm.moore@ucdenver.edu'),
    ('3001000017', 'Joshua', 'Martin', 'j.martin@ucdenver.edu'),
    ('3001000018', 'Melissa', 'Jackson', 'm.jackson@ucdenver.edu'),
    ('3001000019', 'James', 'Thompson', 'j.thompson@ucdenver.edu'),
    ('3001000020', 'Amy', 'White', 'a.white@ucdenver.edu');