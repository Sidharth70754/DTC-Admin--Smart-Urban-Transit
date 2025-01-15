# **Smart Urban Transit Management - Smart Dynamic Bus Scheduling System**

This repository hosts the source code for **Smart Urban Transit Management**, a project developed for the Smart India Hackathon 2024. The solution integrates AI, machine learning, and blockchain technologies to optimize public transportation in Delhi. TransitAI aims to enhance the efficiency of bus scheduling, predictive vehicle maintenance, and crew management using modern tech innovations like blockchain for payment and real-time dynamic scheduling.

## **Repository Structure**

```bash
├── API/
├── Geocoding/
├── ML Models/
├── Web Application/
```

### 1. **API**  
This folder contains the FastAPI backend, which provides APIs for dynamic scheduling, crew management, and predictive maintenance.

- **Features:**
  - Dynamic scheduling API adjusts bus frequencies based on real-time demand.
  - Predictive maintenance API predicts bus maintenance requirements.
  - Crew management API for handling schedules and payments.

### 2. **Geocoding**  
This folder contains scripts to geocode bus stops by converting addresses into latitude and longitude data. 

- **Features:**
  - Geocode bus stop addresses to coordinates.
  - Data preparation for route mapping and optimization.

### 3. **ML Models**  
This folder contains machine learning models used in various aspects of the project.

- **Models:**
  - **CarbonFootprintsTracking**: Calculates and tracks environmental impact.
  - **CrewManagement**: Optimizes crew scheduling.
  - **CrowdDetection**: Detects crowds and dynamically adjusts bus frequencies.
  - **DynamicScheduling**: Predicts bus schedules based on demand patterns.
  - **PredictiveMaintenance**: Predicts the health and maintenance needs of buses.

### 4. **Web Application**  
The frontend for the web application, built using **Next.js** with **Prisma** as the ORM and **TailwindCSS** for styling.

- **Features:**
  - **User Authentication**: Integration with Metamask for crew payments.
  - **Dashboard**: Real-time display of bus frequencies, crew management, and vehicle maintenance.
  - **Blockchain Integration**: Uses Aptos for payment handling.

## **Installation and Setup**

### **Prerequisites**

- Python 3.9+
- Node.js 16+
- PostgreSQL
- Docker (Optional, for containerized setup)
- Aptos SDK

### **Steps to Run the Project**

#### **Backend (FastAPI)**
1. Navigate to the `API` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

#### **Frontend (Next.js)**
1. Navigate to the `Web Application` folder.
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

#### **Geocoding**
1. Navigate to the `Geocoding` folder.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the geocoding script:
   ```bash
   python geocode.py
   ```

#### **Machine Learning Models**
1. Navigate to the `ML Models` folder.
2. Install dependencies for each model.
3. Train or run each model as instructed.

## **Features**

- **AI-Driven Dynamic Scheduling**: Adjust bus schedules based on real-time and historical data.
- **Blockchain for Payments**: Uses Aptos for crew payment management.
- **Predictive Maintenance**: Predict bus failures and maintenance needs.
- **Crowd Detection**: Real-time crowd density detection for bus frequency adjustments.
- **Environmental Monitoring**: Track and reduce carbon emissions using AI.
- **Crew Management**: AI-driven crew scheduling and task management.

## **Usage**

1. **API**: FastAPI server handles all backend logic.
2. **Web Application**: Users interact via a Next.js interface, with real-time data visualizations.
3. **ML Models**: Deployed models dynamically adjust schedules and predict maintenance needs.
4. **Geocoding**: Generates the geographical coordinates of bus stops for routing.

## **Here are some references that could support these points:**

- **DTC Website**: [https://dtc-project.vercel.app/login](https://dtc-project.vercel.app/login)  
  *Email*: admin | *Password*: 123456789 or Login as Admin

- **GitHub**: [https://shorturl.at/sJeFy](https://shorturl.at/sJeFy)

- **Video**: [https://youtu.be/IqWJWaObHxc?si=CNIyX5SvrI_5a0pS](https://youtu.be/IqWJWaObHxc?si=CNIyX5SvrI_5a0pS)

- **Research Paper**: [https://shorturl.at/uAYgk](https://shorturl.at/uAYgk)

- **Model 1**: [https://shorturl.at/qzm3d](https://shorturl.at/qzm3d)  
  *Dataset for Model 1*: [https://shorturl.at/z4KtA](https://shorturl.at/z4KtA)

- **Model 2**: [https://crewwww-abxytwumtpr9dmpgge8ofn.streamlit.app/](https://crewwww-abxytwumtpr9dmpgge8ofn.streamlit.app/)

- **Model 3**: [https://shorturl.at/g0TP](https://shorturl.at/g0TP)


## **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

