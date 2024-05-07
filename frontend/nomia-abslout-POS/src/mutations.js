import gql from 'graphql-tag'

export const USER_SIGNUP = gql`
  mutation ($username: String!, $email: String!, $password: String!) {
    create_user(username: $username, email: $email, password: $password) {
      user {
        id
        username
      }
    }
  }
`

export const USER_SIGNIN = gql`
  mutation ($username: String!, $password: String!) {
    token_auth(username: $username, password: $password) {
      token
      user {
        id
        username
        email
      }
    }
  }
`;

export const UPDATE_USER_PROFILE = gql`
  mutation ($id: ID!) {
    update_user_profile(id: $id) {
      user {
        id
        username
        email
      }
    }
  }
`;

export const SURVEY = gql`
  mutation ($question_text: String!, $description: String, $slug: String!, $active: Boolean) {
    create_survey(question_text: $question_text, description: $description, slug: $slug, active: $active) {
      survey {
        question_text
        description
        active
        slug
      }
    }
  }
`

export const UPDATE_SURVEY = gql`
  mutation ($question_text: String!, $description: String, $active: Boolean, $slug: String, $old_slug: String!) {
    update_survey(question_text: $question_text, description: $description, active: $active, slug: $slug, old_slug: $old_slug) {
      survey {
        question_text
        description
        active
        slug
      }
    }
  }
`

export const CHOICE_SURVEY = gql`
  mutation ($choice_text: String!, $slug: String!) {
    create_survey(choice_text: $choice_text, slug: $slug) {
      choice {
        id_choice
        choice_text
        slug
      }
    }
  }
`

export const UPDATE_CHOICE_SURVEY = gql`
  mutation ($choice_text: String, $slug: String, $old_slug: String!) {
    update_survey_choice(choice_text: $choice_text, slug: $slug) {
      choice {
        id_choice
        choice_text
        slug
      }
    }
  }
`

export const QUESTION = gql`
  mutation ($question_text: String!, $description: String, $slug: String!, $active: Boolean) {
    create_question(question_text: $question_text, description: $description, slug: $slug, active: $active) {
      question {
        question_text
        description
        active
        slug
      }
    }
  }
`

export const UPDATE_QUESTION = gql`
  mutation ($question_text: String!, $description: String, $active: Boolean, $slug: String, $old_slug: String!) {
    update_question(question_text: $question_text, description: $description, active: $active, slug: $slug, old_slug: $old_slug) {
      question {
        question_text
        description
        active
        slug
      }
    }
  }
`

export const CHOICE_QUESTION = gql`
  mutation ($choice_text: String!, $slug: String!) {
    create_question(choice_text: $choice_text, slug: $slug) {
      choice {
        id_choice
        choice_text
        slug
      }
    }
  }
`

export const UPDATE_CHOICE_QUESTION = gql`
  mutation ($choice_text: String, $slug: String, $old_slug: String!) {
    update_question_choice(choice_text: $choice_text, slug: $slug) {
      choice {
        id_choice
        choice_text
        slug
      }
    }
  }
`

export const USER_SURVEY = gql`
  mutation ($id: ID!, $slug: String!, $choices: String!) {
    create_user_survey(id: $id, slug: $slug, choices: $choices) {
      answer_survey {
        survey
        choices
      }
    }
  }
`

export const UPDATE_USER_SURVEY = gql`
  mutation ($id: ID!, $slug: String!, $choices: String!) {
    update_user_survey(id: $id, slug: $slug, choices: $choices) {
      answer_survey {
        survey
        choices
      }
    }
  }
`

export const USER_QUESTION = gql`
  mutation ($id: ID!, $slug: String!, $choices: String!) {
    create_user_question(id: $id, slug: $slug, choices: $choices) {
      answer_question {
        choices
        question
      }
    }
  }
`

export const UPDATE_USER_QUESTION = gql`
  mutation ($id: ID!, $slug: String!, $choices: String!) {
    update_user_question(id: $id, slug: $slug, choices: $choices) {
      answer_question {
        choices
        question
      }
    }
  }
`
