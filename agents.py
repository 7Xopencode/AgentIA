from crewai import Agent, Task, Crew, Process
from crewai_tools import BaseTool, SerperDevTool
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
import os
import json
from get_api_key import get_api_key

os.environ['OPENAI_API_API']="NA"

llm_groq = ChatGroq(temperature=0, groq_api_key=get_api_key()["groq_api_key"],model="llama-3.1-70b-versatile")

file_path="Guide D'orientation 2024-2025.pdf"

# Définition de l'agent IA : son rôle, goal, backstory(contexte), llm, tool
agent = Agent(
    
    role="Conseiller en orientation et insertion professionnelle",
    goal="Proposer des parcours académiques et professionnels en fonction de la filière ou de la spécialité, des matières",
    backstory = "Tu es un agent spécialisé dans le conseil en orientation et insertion professionnel."
    f"Ta mission est de te servir du fichier {file_path} pour proposer des parcours académiques à un utilisateur",
    allow_delegation=False,
     verbose=True,
    llm = llm_groq
  
)

task = Task(
    description= (
       f"Se servir du fichier {file_path} et proposer 5 types de parcours: parcours excéllence, parcours public, parcours privé, parcours normal"
       "Le parcours excéllence est le parcours dans les écoles réputées et bien côtées indépendemment du coût de la formation"
       "Le parcours public est le parcours dans les établissements dont le statut est public"
       "Le parcours privé est le parcours dans les écoles et universités dont le statut est privé"
       "Le parcours normal est le parcours dans les écoles et universités accessibles"
       "Un parcours est représenté par un json de forme : {type : string (different type de parcours) formations: liste d'objet filiere (intitulé filière ou formation,  liste des ecoles proposant la filiere, le domaine d'etude, le niveau d'etude)}"
       
       
       )
    )
   