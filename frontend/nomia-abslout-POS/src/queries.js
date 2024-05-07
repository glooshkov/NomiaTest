import gql from 'graphql-tag'

export const SITE_INFO = gql`
  query {
    site {
      name
    }
  }
`

export const All_SURVEYS = gql`
  query{
    all_surveys {
      id_sur
      question_text
      description
      active
      slug
      choice {
        id_choice
        choice_text
        slug
      }
    }
  }
`

export const All_QUESTIONS = gql`
  query{
    all_questions {
      id_ques
      question_text
      description
      active
      slug
      choice {
        id_choice
        choice_text
        slug
      }
    }
  }
`

export const SURVEY_BY_SLUG = gql`
  query($slug: String!){
    survey_by_slug(slug: $slug) {
      id_sur
      question_text
      description
      active
      slug
    }
  }
`

export const QUESTION_BY_SLUG = gql`
  query($slug: String!) {
    question_by_slug(slug: $slug) {
      id_ques
      question_text
      description
      active
      slug
    }
  }
`

export const CHOICE_SURVEY_BY_SLUG = gql`
  query($slug: String!) {
    choice_survey_by_slug(slug: $slug) {
      id_choice
      survey
      choice_text
      slug
    }
  }
`

export const CHOICE_QUESTION_BY_SLUG = gql`
  query($slug: String!) {
    choice_question_by_slug(slug: $slug) {
      id_choice
      question
      choice_text
      slug
    }
  }
`

export const CURRENT_USER = gql`
  query ($username: String!) {
    currentUser(username: $username) {
      id
      username
      email
      answer_survey {
        choices
      }
      answer_question {
        choices
      }
    }
  }
`;
