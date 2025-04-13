import json
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from llm_helper import llm


def process_posts(raw_json,process_json="data/processed_posts.raw_json"):
    if raw_json == 'Cassie Kozyrkov':
        raw_json = "data/cassie_kozyrkov.json"
    elif raw_json == 'Fabio Moioli':
        raw_json = "data/fabio_moioli.json"
    elif raw_json == 'Helen Yu':
        raw_json = "data/helen_yu.json"
    
    with open(raw_json, encoding = 'utf-8' ) as file:
        posts = json.load(file)
        enriched_posts = []
        for post in posts:
            metadata = extract_metadata(post['text'])
            posts_with_metadata = post | metadata
            print(f'Posts: {post}')
            print(f'Metadata {metadata}')
            enriched_posts.append(posts_with_metadata)
  
        # Normalize unified_tags keys
        unified_tags = get_unified_tags(enriched_posts)
        normalized_unified_tags = {
            key.lower().strip(): value for key, value in unified_tags.items()
        }

        for post in enriched_posts:
            current_tags = post['tags']
            new_tags = {
                normalized_unified_tags.get(tag.lower().strip(), tag)  # Fallback if tag not found
                for tag in current_tags
            }

            post['tags'] = list(new_tags)

        with open('data/processed_posts.json', encoding='utf-8', mode= 'w') as outputfile:
            json.dump(enriched_posts,outputfile,indent=4)



def get_unified_tags(posts_with_metadata):
    unique_tags = set()
    for post in posts_with_metadata:
        unique_tags.update(post['tags'])

    unique_tag_list = ', '.join(unique_tags)

    template = ''' I will give you a list of tags you need to unify them with the following requirement,
    1.  tags are unified and merged to create a shorter list.
        Example 1 "Job Seeker", "Jobhunter" All can be unified as single tag Job Search.
        Example 2 "Motivation", "Inspiration" "Drive" can be mapped as Motivation.
        Example 3 "Personal Growth", "Personal Development", "Self Improvement" can be classified as Self Improvement
        Example 4 "scam Alert", "Job Scam" as Scam
    2.  Each Tag should follow title case convention like: "Job Search", "Motivation"
    3.  Output should be a json object No Preamble.
    4.  Output should have mapping of original Tags and Unified Tags.
        Example: {{"Job Seaker": "Job Search", "Inspiration": "Motivation" }}

        Here is the List of Tags
        {tags}

    '''
    pt = PromptTemplate.from_template(template)

    chain = pt | llm
    response = chain.invoke(input = {'tags':str(unique_tag_list)})

    try:
        Json_parser = JsonOutputParser()
        res = Json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException('Content to big unable to parse job')

    return res


def extract_metadata(post):
    template = '''
            I am providing you a Linkedin post, you need to exract number of lines in post, Langauage
            of the post, and tags
            1. Return a valid Json, No Preable.
            2.Json Object should have exactly 3 keys, Line_count, Language, tags.
            3.Tags in an array of tags, extract maximum 2 tags.
            4.Language should be English or Roman Urdu(write urdu in English Script).

            here is an actual post on which you need to perform these tasks.
            {post}
    '''
    pt = PromptTemplate.from_template(template)

    chain = pt | llm
    response = chain.invoke(input = {'post':post})

    try:
        Json_parser = JsonOutputParser()
        res = Json_parser.parse(response.content)
    except OutputParserException:
        raise OutputParserException('Content to big unable to parse job')

    return res
one = "data/raw_post.json"
two = "data/raw_post1.json"
three = "data/raw_post3.json"
if __name__ == "__main__":
    process_posts('3',"processed_posts.json")

