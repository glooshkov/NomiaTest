<template>
  <div class="parent">
    <div class="container">
      <h2 class="title">Завершите регистрацию</h2>
    </div>

    <div class="box">
      <form method="POST"  @submit.prevent="userSignUp">

        <div v-for="question in activeQuestions" :key="question.id_ques" style="margin-left: auto; margin-right: auto;">
          <label v-if="question.slug === 'type'" class="text-block">{{ question.question_text }}</label>
          <div v-if="question.slug === 'type'">
            <label v-for="(choice, index) in question.choice" :key="index" class="choices">
              <input type="checkbox" @change="choose(choice.slug, 'type')" :value="choice" :checked="isSelected(choice.slug, 'type')"/>
              {{ choice.choice_text }}
            </label>
          </div>
        </div>

        <div v-for="question in activeQuestions" :key="question.id_ques">
          <label v-show="userDetails.type === question.slug" class="text-block">{{ question.question_text }}</label>
          <div v-show="userDetails.type === question.slug">
            <label v-for="(choice, index) in question.choice" :key="index" class="choices">
              <input type="checkbox" @change="choose(choice.slug, 'kind')" :value="choice" :checked="isSelected(choice.slug, 'kind')"/>
              {{ choice.choice_text }}
            </label>
          </div>
        </div>

        <div v-for="question in activeSurveys" :key="question.id_sur">
          <label v-show="returnBoolean(question.slug, 'elements')" class="text-block">{{ question.question_text }}</label>
          <div v-show="returnBoolean(question.slug, 'elements')">
            <label v-for="(choice, index) in question.choice" :key="index" class="choices">
              <input type="checkbox" @change="choose(choice.id_choice, 'elements')" :value="choice" :checked="isSelected(choice.id_choice, 'elements')"/>
              {{ choice.choice_text }}
            </label>
          </div>
        </div>

        <div v-for="question in activeSurveys" :key="question.id_sur">
          <label v-show="returnBoolean(question.slug, 'settings')" class="text-block">{{ question.question_text }}</label>
          <div v-show="returnBoolean(question.slug, 'settings')">
            <label v-for="(choice, index) in question.choice" :key="index" class="choices">
              <input type="checkbox" @change="choose(choice.id_choice, 'settings')" :value="choice" :checked="isSelected(choice.id_choice, 'settings')"/>
              {{ choice.choice_text }}
            </label>
          </div>
        </div>

        <div>
          <my-button type="submit" style="margin-top: 1.5rem;">ЗАВЕРШИТЬ</my-button>
        </div>
      </form>

    </div>
  </div>
</template>


<script>
import {USER_SURVEY, USER_QUESTION} from "@/mutations";
import MyButton from "@/views/UI/MyButton.vue";
import {All_SURVEYS, All_QUESTIONS} from "@/queries.js";

export default {
  name: "OnboardingView",
  components: {MyButton},
  data() {
    return {
      userDetails: {},

      // ПРИМЕРЫ созданных вопосов и ответов
      activeSurveys: [
        // {
        //   id_sur: 1,
        //   question_text: 'Какие элементы вам понадобятся для работы?',
        //   description: 'Какое-то описание...',
        //   active: true,
        //   slug: 'elements',
        //   choice: [{id_choice: 1, choice_text: 'Элемент 1', slug: 'element-1'},{id_choice: 2, choice_text: 'Элемент 2', slug: 'element-2'},{id_choice: 3, choice_text: 'Элемент 3', slug: 'element-3'}]
        // },
        // {
        //   id_sur: 2,
        //   question_text: 'Настройка личного профиля',
        //   description: 'Какое-то описание...',
        //   active: true,
        //   slug: 'settings',
        //   choice: [{id_choice: 1, choice_text: 'Настройка 1', slug: 'nastroyka-1'},{id_choice: 2, choice_text: 'Настройка 2', slug: 'nastroyka-2'},{id_choice: 3, choice_text: 'Настройка 3', slug: 'nastroyka-3'}]
        // }
      ],
      activeQuestions: [
        // {
        //   id_ques: 1,
        //   question_text: 'Выберите тип вашего бизнеса',
        //   description: 'Какое-то описание...',
        //   active: true,
        //   slug: 'type',
        //   choice: [{id_choice: 1, choice_text: 'Общепит', slug: 'obshepit'},{id_choice: 2, choice_text: 'Ритейл', slug: 'riteyl'},{id_choice: 3, choice_text: 'Услуги по записи', slug: 'zapis'}]
        // },
        // {
        //   id_ques: 2,
        //   question_text: 'Выберите вид вашего бизнеса',
        //   description: 'Какое-то описание...',
        //   active: true,
        //   slug: 'obshepit',
        //   choice: [{id_choice: 1, choice_text: 'Бар', slug: 'bar'},{id_choice: 2, choice_text: 'Кофейня', slug: 'cofeynya'},{id_choice: 3, choice_text: 'Ресторан', slug: 'restoran'}]
        // },
        // {
        //   id_ques: 3,
        //   question_text: 'Выберите вид вашего бизнеса',
        //   description: 'Какое-то описание...',
        //   active: true,
        //   slug: 'riteyl',
        //   choice: [{id_choice: 1, choice_text: 'Магазин бытовой техники', slug: 'tehnika'},{id_choice: 2, choice_text: 'Аптека', slug: 'apteka'},{id_choice: 3, choice_text: 'Книжный магазин', slug: 'knizhniy'}]
        // },
        // {
        //   id_ques: 4,
        //   question_text: 'Выберите вид вашего бизнеса',
        //   description: 'Какое-то описание...',
        //   active: true,
        //   slug: 'zapis',
        //   choice: [{id_choice: 1, choice_text: 'Салон красоты', slug: 'krasoty'},{id_choice: 2, choice_text: 'Парикмахерская', slug: 'parikmaherskaya'},{id_choice: 3, choice_text: 'Спа-салон', slug: 'spa'}]
        // }
      ],
    };
  },

  async created() {
    try {
      const survey = await this.$apollo.query({
        query: All_SURVEYS,
      });
      this.activeSurveys = survey.data.all_surveys;
      this.activeSurveys.forEach(item => {
        this.userDetails[item.slug] = [];
      })

      const question = await this.$apollo.query({
        query: All_QUESTIONS,
      });
      this.activeQuestions = question.data.all_questions;
      this.activeQuestions.forEach(item => {
        this.userDetails[item.slug] = '';
      })

    } catch (error) {
      console.error('Ошибка при создании хука:', error);
    }

  },
  methods: {
    async userSignUp() {
      const slugQuestion = ['type', 'kind']
      const slugSurvey = ['elements', 'settings']
      for (const slug of slugSurvey) {
        const propString = this.userDetails[slug].join('-');
        try {
          const survey = await this.$apollo.mutate({
            mutation: USER_SURVEY,
            variables: {
              id: 1,
              slug: slug,
              choices: propString,
            },
          });
        } catch (error) {
          console.error(`Ошибка при выполнении мутации для слага '${slug}':`, error);
        }
      }

      for (const slug of slugQuestion) {
        try {
          const question = await this.$apollo.mutate({
            mutation: USER_QUESTION,
            variables: {
              id: 1,
              slug: slug,
              choices: this.userDetails[slug],
            },
          });
        } catch (error) {
          console.error(`Ошибка при выполнении мутации для слага '${slug}':`, error);
        }
      }
    },
    choose(slug, prop){
      if (prop === 'type' || prop === 'kind') {
        this.userDetails[prop] = slug;
      } else {
        const index = this.userDetails[prop].indexOf(slug);
        if (index !== -1) {
            this.userDetails[prop].splice(index, 1);
        } else {
          this.userDetails[prop].push(slug)
        }
        console.log(this.userDetails[prop].length, slug)
      }
      return this.userDetails[prop]
    },
    isSelected(slug, prop) {
      return this.userDetails[prop] === slug;
    },
    returnBoolean(slug, prop){
      return !!(this.userDetails.kind && slug === prop)
    },
  },
};
</script>

<style>

</style>
