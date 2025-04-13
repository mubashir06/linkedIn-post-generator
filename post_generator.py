from llm_helper import llm
from few_shot import FewShotPosts



def get_length_str(length):
    if length == "short":
        return "1 to 3 lines"
    elif length == "medium":
        return "3 to 8 lines"
    elif length == "long":
        return "more than 8 lines"
        

few_shot_post = FewShotPosts()

def get_prompt(length, language, tag):
    length_str = get_length_str(length)
    if language == "English":
        prompt = f'''
        Generate a LinkedIn Post using the information Below, No preamble.
        1) topic: {tag}
        2) length: {length_str}
        3) language: {language}.

        '''
    
        example = few_shot_post.get_filtered_post(length,language,tag)
        if len(example)>0:
            prompt += "4) Use the writting style as per following examples."
            for i, post in enumerate(example):
                post_text = post['text']
                prompt += f"\n\n Example: {i+1}: {post_text}" 
                if i == 2:
                    break
    elif language == "Roman Urdu":
        prompt = f'''
        Generate a LinkedIn Post using the information Below, No preamble.
        1) topic: {tag}
        2) length: {length_str}
        3) language: {language}

        when language is Roman Urdu write in urdu its kind of mixture of both english and urdu,
        script should always be English. use human language.

        '''
      
        example = few_shot_post.get_filtered_post(length,language,tag)
        if len(example)>0:
            prompt += "4) Use the writting style as per following examples."
            for i, post in enumerate(example):
                post_text = post['text']
                prompt += f"\n\n Example: {i+1}: {post_text}" 
                if i == 2:
                    break
        prompt = f'''
        Generate a LinkedIn Post using the information Below, No preamble.
        1) topic: {tag}
        2) length: {length_str}
        3) language: {language}

        when language is Roman Urdu write in urdu its kind of mixture of both english and urdu,
        script should always be English and when Language is English use english. use human language.

        '''
        example = few_shot_post.get_filtered_post(length,language,tag)
        if len(example)>0:
            prompt += "4) Use the writting style as per following examples."
            for i, post in enumerate(example):
                post_text = post['text']
                prompt += f"\n\n Example: {i+1}: {post_text}" 
                if i == 2:
                    break

    return prompt

def generate_post(length, language, tag):
    prompt = get_prompt(length, language, tag)
    response = llm.invoke(prompt)

    return response.content


if __name__ == '__main__':
    post = generate_post('short', 'Roman Urdu','Career Advice')
    
    print(post)
