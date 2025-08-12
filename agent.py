import os
import sqlite3
import pandas as pd

# CSV file paths
heart_csv = r"C:\Users\Mehedi\Desktop\heart.csv"
cancer_csv = r"C:\Users\Mehedi\Desktop\The_Cancer_data_1500_V2.csv"
diabetes_csv = r"C:\Users\Mehedi\Desktop\diabetes.csv"

# --- CSV to SQLite Converter ---
class CSVToSQLiteConverter:
    """Converts CSV files to SQLite databases"""
    
    @staticmethod
    def convert_csv_to_sqlite(csv_path, db_name, database_folder="databases"):
        try:
            os.makedirs(database_folder, exist_ok=True)
            
            # Read CSV file
            df = pd.read_csv(csv_path)
            
            # Create database path
            db_path = os.path.join(database_folder, f"{db_name}.db")
            
            # Connect to SQLite database
            conn = sqlite3.connect(db_path)
            
            # Convert DataFrame to SQLite table
            table_name = db_name.lower().replace('_', '')
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            
            conn.close()
            return True, f"Successfully converted {csv_path} to {db_path}"
        except Exception as e:
            return False, f"Error converting CSV: {str(e)}"

# --- Base Database Query Tool ---
class DatabaseQueryTool:
    def __init__(self, db_path, table_name):
        self.db_path = db_path
        self.table_name = table_name
    
    def execute_query(self, query):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            conn.close()
            return True, {"columns": columns, "data": results}
        except Exception as e:
            return False, f"Database query error: {str(e)}"

# --- Heart Disease Tool ---
class HeartDiseaseDBTool(DatabaseQueryTool):
    def __init__(self, database_folder="databases"):
        db_path = os.path.join(database_folder, "heart.db")
        super().__init__(db_path, "heart")
    
    def analyze_question(self, question):
        q = question.lower()
        if "average age" in q or "mean age" in q:
            return "SELECT AVG(age) as average_age FROM heart"
        elif "count" in q and "heart disease" in q:
            return "SELECT COUNT(*) as total_patients FROM heart WHERE target = 1"
        elif "cholesterol" in q and "average" in q:
            return "SELECT AVG(chol) as average_cholesterol FROM heart"
        elif "age distribution" in q:
            return "SELECT age, COUNT(*) as count FROM heart GROUP BY age ORDER BY age"
        else:
            return f"SELECT * FROM heart LIMIT 10"

# --- Cancer Tool ---
class CancerDBTool(DatabaseQueryTool):
    def __init__(self, database_folder="databases"):
        db_path = os.path.join(database_folder, "cancer.db")
        super().__init__(db_path, "thecancerdata1500v2")
    
    def analyze_question(self, question):
        q = question.lower()
        if "average age" in q:
            return "SELECT AVG(Age) as average_age FROM thecancerdata1500v2"
        elif "smoking" in q and "cancer" in q:
            return "SELECT Smoking, COUNT(*) as count FROM thecancerdata1500v2 WHERE Diagnosis = 1 GROUP BY Smoking"
        elif "gender distribution" in q:
            return "SELECT Gender, COUNT(*) as count FROM thecancerdata1500v2 GROUP BY Gender"
        elif "bmi" in q and "average" in q:
            return "SELECT AVG(BMI) as average_bmi FROM thecancerdata1500v2"
        else:
            return f"SELECT * FROM thecancerdata1500v2 LIMIT 10"

# --- Diabetes Tool ---
class DiabetesDBTool(DatabaseQueryTool):
    def __init__(self, database_folder="databases"):
        db_path = os.path.join(database_folder, "diabetes.db")
        super().__init__(db_path, "diabetes")
    
    def analyze_question(self, question):
        q = question.lower()
        if "average glucose" in q:
            return "SELECT AVG(Glucose) as average_glucose FROM diabetes"
        elif "diabetes count" in q:
            return "SELECT COUNT(*) as diabetic_patients FROM diabetes WHERE Outcome = 1"
        elif "age distribution" in q:
            return "SELECT Age, COUNT(*) as count FROM diabetes GROUP BY Age ORDER BY Age"
        elif "bmi" in q and "average" in q:
            return "SELECT AVG(BMI) as average_bmi FROM diabetes"
        else:
            return f"SELECT * FROM diabetes LIMIT 10"

# --- Medical Web Search Tool (Offline) ---
class MedicalWebSearchTool:
    @staticmethod
    def search_medical_info(query):
        q = query.lower()
        if "symptoms" in q:
            if "heart" in q:
                return True, "Heart disease symptoms: chest pain, shortness of breath, fatigue..."
            elif "cancer" in q:
                return True, "Cancer symptoms: weight loss, fatigue, lumps..."
            elif "diabetes" in q:
                return True, "Diabetes symptoms: thirst, urination, fatigue..."
        return True, f"No specific answer for '{query}'"

# --- Main AI Agent ---
class MedicalAIAgent:
    def __init__(self, database_folder="databases"):
        self.heart_tool = HeartDiseaseDBTool(database_folder)
        self.cancer_tool = CancerDBTool(database_folder)
        self.diabetes_tool = DiabetesDBTool(database_folder)
        self.web_search_tool = MedicalWebSearchTool()
    
    def route_question(self, question):
        q = question.lower()
        data_keywords = ["count", "average", "mean", "distribution", "statistics", "data", "number", "percentage"]
        general_keywords = ["symptoms", "treatment", "cure", "what is", "definition", "causes"]
        
        is_data = any(k in q for k in data_keywords)
        is_general = any(k in q for k in general_keywords)
        
        if is_data:
            if "heart" in q:
                return self._query_database(self.heart_tool, question)
            elif "cancer" in q:
                return self._query_database(self.cancer_tool, question)
            elif "diabetes" in q:
                return self._query_database(self.diabetes_tool, question)
            else:
                return "Please specify dataset: heart, cancer, or diabetes."
        
        elif is_general:
            success, result = self.web_search_tool.search_medical_info(question)
            return result if success else "Web search failed."
        
        else:
            return "Please ask about data statistics or medical info."
    
    def _query_database(self, db_tool, question):
        try:
            sql_query = db_tool.analyze_question(question)
            success, result = db_tool.execute_query(sql_query)
            if success:
                cols = result["columns"]
                data = result["data"]
                if len(data) == 1 and len(cols) == 1:
                    return f"The result is: {data[0][0]}"
                elif len(data) <= 10:
                    return "\n".join(str(dict(zip(cols, row))) for row in data)
                else:
                    return f"Found {len(data)} results. First few: {data[:5]}"
            else:
                return f"Error: {result}"
        except Exception as e:
            return f"Error processing: {str(e)}"


# Convert CSVs at startup
CSVToSQLiteConverter.convert_csv_to_sqlite(heart_csv, "heart")
CSVToSQLiteConverter.convert_csv_to_sqlite(cancer_csv, "cancer")
CSVToSQLiteConverter.convert_csv_to_sqlite(diabetes_csv, "diabetes")

# Example usage
if __name__ == "__main__":
    agent = MedicalAIAgent()
    print(agent.route_question("What is the average age in heart dataset?"))
    print(agent.route_question("What are the symptoms of cancer?"))
