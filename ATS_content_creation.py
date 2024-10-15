import json
import boto3
from dotenv import load_dotenv
import os
import logging
from botocore.exceptions import ClientError
from json import JSONDecodeError
load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def generate_ats_projects(projects_json, job_description, ats_suggestions_json):
    logging.info("Projects Generation")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "projects": {
              "names": [
                  "",
                  "",
                  ""
              ],
              "descriptions": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ],
              "dates": [
                  "",
                  "",
                  ""
              ],
              "technologies": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for rewriting projects section based on resume text and job description in ATS friendly way, in json format."
    prompt = f"Enhance the projects section to maximize the ATS score (aiming for 95-100) based on the provided job description. " \
             f"Current projects section: {projects_json}. " \
             f"Job description: {job_description}" \
             f"Utilize the suggestions from a previous ATS scan, which includes scores, keywords insights, missing keywords, resume ranking, and flagged issues in the following JSON format: {ats_suggestions_json}. " \
             f"Highlight relevant tools, technologies, and techniques utilized in each project. " \
             f"Emphasize quantifiable results and the overall impact of the projects, particularly outcomes that align with the job requirements. " \
             f"Ensure that all projects directly relate to the job description, omitting irrelevant details and focusing on what matters. " \
             f"Maintain clear, concise, and action-oriented descriptions, utilizing industry-specific terminology where appropriate. " \
             f"Return any sections or fields not applicable in the example output JSON format, preserving empty lists as required. " \
             f"Strictly return the output in the format of a Python dictionary or JSON same as example without any additional text or explanation."

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Projects Done")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_


def generate_ats_experience(experience_json, job_description, ats_suggestions_json):
    logging.info("Experience Generation")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "experiences": {
              "company_names": [
                  "",
                  "",
                  ""
              ],
              "positions": [
                  "",
                  "",
                  ""
              ],
              "descriptions": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ],
              "durations": [
                  "",
                  "",
                  ""
              ],
              "locations": [
                  "",
                  "",
                  ""
              ],
              "technologies": [
                  ["", "", ""],
                  ["", "", ""],
                  ["", "", ""]
              ],
              "achievements": [
                  "",
                  "",
                  ""
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for rewriting experiences section based on resume text and job description in ATS friendly way, in json format."
    prompt = f"Enhance the experience section to maximize the ATS score (aiming for 95-100) based on the provided job description. " \
             f"Current experience section: {experience_json}. " \
             f"Job description: {job_description}" \
             f"Utilize the suggestions from a previous ATS scan, which includes scores, keywords insights, missing keywords, resume ranking, and flagged issues in the following JSON format: {ats_suggestions_json}. " \
             f"Match relevant responsibilities and achievements from the job description to the candidate’s experience. " \
             f"Utilize action verbs and industry-specific terminology found in the job description to articulate the candidate’s accomplishments. " \
             f"Quantify achievements with specific metrics and results (e.g., percentage improvements, revenue impacts, efficiency gains) to demonstrate effectiveness. " \
             f"Highlight the most relevant experiences and responsibilities to ensure alignment with the job description. " \
             f"Avoid generic or irrelevant details while maintaining clarity and conciseness. " \
             f"Return any sections or fields not applicable in the example output JSON format, preserving empty lists as required. " \
             f"Strictly return the output in the format of a Python dictionary or JSON same as example without any additional text or explanation."

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Experience Done")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_


def generate_ats_skills(skills_json, job_description, ats_suggestions_json):
    logging.info("Skills Generation")
    bedrock = boto3.client(service_name="bedrock-runtime",
                           aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
                           aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
                           region_name="us-east-1")

    model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
    example_response = {
          "skills": {
              "technical_skills": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "tools/frameworks": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "soft_skills": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "analytical_skills": [
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  "",
                  ""
              ],
              "spoken_languages": [
                  "",
                  "",
                  ""
              ]
          }
    }

    accept = "application/json"
    contentType = "application/json"
    content = "You are a helpful assistant for rewriting skills section based on resume text and job description in ATS friendly way, in json format."
    prompt = f"Enhance the skills section to maximize the ATS score (aiming for 95-100) based on the provided job description. " \
             f"Current skills section: {skills_json}. " \
             f"Job description: {job_description}" \
             f"Utilize the suggestions from a previous ATS scan, which includes scores, keywords insights, missing keywords, resume ranking, and flagged issues in the following JSON format: {ats_suggestions_json}. " \
             f"Match relevant hard skills and soft skills from the job description, including any synonyms or variations of skills. " \
             f"Prioritize skills that are mentioned multiple times or labeled as essential in the job description. " \
             f"Avoid adding irrelevant or overly generic skills. " \
             f"If any skills mentioned in the example output JSON are missing from the enhanced section, return empty strings in the same format. " \
             f"Strictly return the output in the format of a Python dictionary or JSON same as example without any additional text or explanation."

    try:
        response = bedrock.invoke_model(
              modelId=model_id,
              body=json.dumps(
                  {
                      "anthropic_version": "bedrock-2023-05-31",
                      "max_tokens": 1024,
                      "messages": [
                          {"role": "user",
                           "content": f"{content}"},
                          {"role": "assistant",
                           "content": f"{prompt}"},
                          {"role": "user",
                           "content": f"Example response:\n{json.dumps(example_response, indent=4)}"}

                      ],
                  }),
              accept=accept,
              contentType=contentType
          )
        result = json.loads(response.get('body').read())
        content = result['content'][0]['text']
        j_ = json.loads(content)
        logging.info("Skills Done")
    except Exception as e:
        if isinstance(e, ClientError):
            logging.error(f"SERVERSIDE ERROR OCCURRED: {e}")
            j_ = ""
        elif isinstance(e, JSONDecodeError):
            logging.error("JSON ERROR OCCURRED")
            j_ = ""
        else:
            logging.error(f"{e}")
            j_ = ""
    return j_

