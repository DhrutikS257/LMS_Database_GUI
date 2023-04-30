
import sqlite3
# conn = sqlite3.connect('Database.db')

# # Create a cursor object
# c = conn.cursor()

# # Execute the ALTER TABLE statement to add a new column
# c.execute('ALTER TABLE BOOK_LOANS ADD COLUMN Late BOOLEAN NULL')

# # Commit the changes to the database
# conn.commit()

# # Close the cursor and connection
# c.close()
# conn.close()



conn = sqlite3.connect('Database.db')

# Create a cursor object
c = conn.cursor()

# Execute the ALTER TABLE statement to add a new column
c.execute('ALTER TABLE LIBRARY_BRANCH ADD COLUMN LateFee FLOAT DEFAULT 0')

# Commit the changes to the database
conn.commit()

# Close the cursor and connection
c.close()
conn.close()















