-- Prints the full description of a table
SELECT dbms_metadata.get_ddl('TABLE', 'first_table', 'root') from hbtn_0c_0;
