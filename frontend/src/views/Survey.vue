<template>
  <div class="survey">
    <div class="survey-box">
      <h1>설문 조사</h1>
      <h4>
        여러분에게 꼭 맞는 문화재를 추천해드리기 위해 필요한 설문조사입니다!
      </h4>
      <h4>시간을 내서 끝까지 진행해주시면 감사하겠습니다!</h4>

      <v-container>
        <!-- 시대 -->
        <v-row>
          <v-col cols="12" sm="4">
            <v-subheader v-text="'시대별 선호도 조사'"></v-subheader>
          </v-col>

          <v-col cols="12" sm="8">
            <v-select
              v-model="e5"
              :items="era"
              label="선택"
              multiple
              chips
              hint="당신이 좋아하는 시대는 무엇인가요?"
              persistent-hint
            ></v-select>
          </v-col>
        </v-row>

        <!-- 인물 -->
        <v-row>
          <v-col cols="12" sm="4">
            <v-subheader v-text="'인물별 선호도 조사'"></v-subheader>
          </v-col>

          <v-col cols="12" sm="8">
            <v-select
              v-model="e6"
              :items="people"
              label="선택"
              multiple
              chips
              hint="알고 싶은 특별한 인물이 있나요?"
              persistent-hint
            ></v-select>
          </v-col>
        </v-row>

        <!-- 문화재 종류 -->
        <v-row>
          <v-col cols="12" sm="4">
            <v-subheader v-text="'문화재 종류 선호도 조사'"></v-subheader>
          </v-col>

          <v-col cols="12" sm="8">
            <v-select
              v-model="e7"
              :items="heritages"
              label="선택"
              multiple
              chips
              hint="좋아하는 문화재에는 어떤 것이 있나요?"
              persistent-hint
            ></v-select>
          </v-col>
        </v-row>
      </v-container>

      <br />
      <v-btn>제 to the 출</v-btn>
    </div>
  </div>
</template>

<script>
import "@/assets/css/views/survey.scss";

export default {
  name: "Survey",
  data() {
    return {
      e5: [],
      e6: [],
      e7: [],
      era: [
        "청동기시대",
        "철기시대",
        "삼국시대",
        "통일신라",
        "남북국시대",
        "고려시대",
        "조선시대",
      ],
      people: ["세종대왕", "영조", "정조", "태종", "장영실", "주몽"],
      heritages: [
        "불상",
        "백자",
        "청자",
        "토기",
        "석탑",
        "목탑",
        "절",
        "고궁",
        "절터",
        "탱화",
        "벽화",
        "가구",
      ],
    };
  },
};
</script>

