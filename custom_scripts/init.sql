CREATE USER improvs_test_task_dev WITH PASSWORD 'improvs_test_task_dev';
ALTER USER improvs_test_task_dev CREATEDB;
CREATE DATABASE improvs_test_task_dev WITH OWNER improvs_test_task_dev;
GRANT ALL PRIVILEGES ON DATABASE improvs_test_task_dev TO improvs_test_task_dev;
