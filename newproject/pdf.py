import markdown2
from fpdf import FPDF

# Define the document content
document_content = """
# High-Level Design Document for Cricket API

## Table of Contents

1. **Introduction**
   1.1 Purpose
   1.2 Scope

2. **System Overview**

3. **Architecture**
   3.1 High-Level Architecture Diagram
   3.2 Components

4. **Frontend Design**
   4.1 Structure
   4.2 Routing
   4.3 Key Components

5. **Backend Design**
   5.1 Structure
   5.2 API Endpoints

6. **Database Design**
   6.1 Schema
   6.2 Relationships

7. **Third-Party API Integration**

8. **Security**

9. **Deployment**

10. **Conclusion**

### Detailed Sections

1. **Introduction**
   - **1.1 Purpose**
     This document provides a high-level overview of the Cricket API system. It details the architecture, design, and interactions between different components, serving as a guide for developers and stakeholders.
   - **1.2 Scope**
     The document covers the architectural design, including frontend, backend, and database components. It explains how these components interact and integrates third-party APIs for live scores. Security and deployment processes are also discussed.

2. **System Overview**
   The Cricket API system is designed to provide real-time cricket match information. It allows users to register, login, and view match schedules. Administrators can manage matches, and the system integrates with third-party APIs to fetch live scores.

3. **Architecture**
   - **3.1 High-Level Architecture Diagram**
     The high-level architecture diagram illustrates the interaction between the frontend, backend, and database. It shows how the frontend communicates with the backend via API endpoints and how the backend interacts with the database.
   - **3.2 Components**
     - **Frontend:** Built with React, handles user interface and interactions.
     - **Backend:** Developed using Node.js, manages API endpoints and business logic.
     - **Database:** Stores user and match data, uses MongoDB for flexibility and scalability.
     - **Third-Party API:** Provides live scores, integrated into the backend.

4. **Frontend Design**
   - **4.1 Structure**
     The frontend application is structured as follows:
     - **components/**: Reusable UI components like LiveScore and MatchCard.
     - **pages/**: Main pages including Home, Login, Register, MatchSchedule, and AdminDashboard.
     - **assets/**: Static assets such as images and styles.
   - **4.2 Routing**
     Routing is managed using React Router. Below is an example from `App.jsx`:

     ```jsx
     import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
     import Home from './pages/Home.jsx';
     import MatchSchedule from './pages/MatchSchedule.jsx';
     import Login from './pages/Login.jsx';
     import Register from './pages/Register.jsx';
     import AdminDashboard from './pages/AdminDashboard.jsx';

     function App() {
       return (
         <Router>
           <Routes>
             <Route path="/" element={<Home />} />
             <Route path="/login" element={<Login />} />
             <Route path="/match-schedule" element={<MatchSchedule />} />
             <Route path="/register" element={<Register />} />
             <Route path="/admindashboard" element={<AdminDashboard />} />
           </Routes>
         </Router>
       );
     }

     export default App;
     ```

   - **4.3 Key Components**
     - **Home:** Main landing page.
     - **Login:** User authentication.
     - **Register:** User registration.
     - **MatchSchedule:** Displays upcoming matches.
     - **AdminDashboard:** Admin functionalities for managing matches.

5. **Backend Design**
   - **5.1 Structure**
     The backend application is organized as follows:
     - **controllers/**: Handles incoming requests and business logic.
     - **models/**: Defines database schemas.
     - **routes/**: Maps endpoints to controllers.
     - **middlewares/**: Custom middleware functions.
   - **5.2 API Endpoints**
     - **/api/login**: Authenticates user.
     - **/api/register**: Registers new user.
     - **/api/admin/addmatch**: Adds a new match (Admin only).
     - **/api/admin/getmatch**: Retrieves match information.
     - **/api/userauth**: Authenticates users for protected routes.

6. **Database Design**
   - **6.1 Schema**
     The MongoDB database includes the following collections:
     - **users**
       ```json
       {
         "name": "string",
         "email": "string",
         "password": "string",
         "role": "string"
       }
       ```
     - **matches**
       ```json
       {
         "teams": ["string"],
         "date": "Date",
         "venue": "string",
         "status": "string"
       }
       ```

   - **6.2 Relationships**
     There are no direct foreign key relationships due to the NoSQL nature of MongoDB, but logical relationships exist:
     - Users and matches are linked by user roles (admin, user).

7. **Third-Party API Integration**
   The system integrates with third-party APIs to fetch live scores. The backend periodically calls these APIs and updates the match status in the database.

8. **Security**
   Security measures include:
   - **Authentication:** JWT for securing endpoints.
   - **Authorization:** Role-based access control.
   - **Data Protection:** Encryption of sensitive data like passwords.

9. **Deployment**
   The application is deployed using the following processes:
   - **Frontend:** Deployed on a web server (e.g., Vercel, Netlify).
   - **Backend:** Deployed on a server (e.g., Heroku, AWS).
   - **Database:** Hosted on a cloud database service (e.g., MongoDB Atlas).

10. **Conclusion**
    This document provides a comprehensive overview of the Cricket API system's high-level design. Future iterations will include more detailed designs and implementation specifics.
"""

# Convert the markdown content to HTML
html_content = markdown2.markdown(document_content)

# Create a PDF
pdf = FPDF()

# Add a page
pdf.add_page()

# Set font
pdf.set_font("Arial", size=12)

# Convert HTML to text
text_content = html_content.replace('<h1>', '').replace('</h1>', '').replace('<h2>', '').replace('</h2>', '').replace('<strong>', '').replace('</strong>', '').replace('<ul>', '').replace('</ul>', '').replace('<li>', '').replace('</li>', '').replace('<p>', '').replace('</p>', '').replace('<br>', '\n').replace('&nbsp;', ' ')

# Split text into lines
lines = text_content.split('\n')

# Add text to PDF
for line in lines:
    pdf.multi_cell(0, 10, line)

# Save the PDF to a file
pdf_output = "High_Level_Design_Document_for_Cricket_API.pdf"
pdf.output(pdf_output)
