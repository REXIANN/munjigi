<template>
  <div class="mypageProfile">
    <h1>{{ userData.user.nickname }}님의 마이페이지</h1>
    <v-row justify="space-between">
      <v-col>
        <img :src="userImage" />
        <div>
          <input type="file" @change="previewImage" accept="image/*" />
        </div>
        <div>
          <p>
            미리보기 준비 중 : {{ uploadValue.toFixed() + "%" }}
            <progress id="progress" :value="uploadValue" max="100"></progress>
          </p>
          <v-btn @click="submitFile">업로드하기</v-btn>
        </div>
      </v-col>
      <v-col>
        <h3>이름 : {{ userData.name }}</h3>
        <h3>성씨 본관 :{{ userData.lastname }}</h3>
        <div>
          <v-btn @click="searchAncestor(userData.ancestor)"
            >조상과 관련된 문화재 보기</v-btn
          >
        </div>
      </v-col>
      <v-col>
        <h3>현재 신분 {{ userData.grade }}</h3>
        <!-- <v-img
          class="grade-image"
          src="https://user-images.githubusercontent.com/60081201/93740775-20f36400-fc26-11ea-96ed-417389ec29eb.png"
          alt="양반등급 이미지"
          height="100px"
          width="100px"
        />-->
        <v-dialog v-model="gradeInfo" width="600px">
          <template v-slot:activator="{ on, attrs }">
            <v-btn
              class="ma-2"
              tile
              outlined
              color="success"
              v-bind="attrs"
              v-on="on"
              >신분제알아보기</v-btn
            >
          </template>
          <v-card>
            <v-card-title>
              <span class="headline">문지기의 신분제</span>
              리뷰수로 신분이 결정됩니다.
            </v-card-title>
            <v-card-text>
              왕 : 리뷰 50개 이상 / 영의정 : 리뷰 30개 이상 / 기미상궁 : 리뷰
              20개 이상 / 사또 : 리뷰 10개 이상 / 양반 : 리뷰 5개 이상 / 천민 :
              리뷰 0개 이상
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="green darken-1" text @click="gradeInfo = false"
                >닫기</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import SERVER from "@/api/drf";
import axios from "axios";
import firebase from "firebase";

export default {
  name: "MypageProfile",
  mounted() {
    axios
      .get(SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/")
      .then((res) => {
        this.userData = res.data;
        this.userImage = res.data.profile_image;
      })
      .catch((err) => console.log(err));
  },
  methods: {
    previewImage(event) {
      this.uploadValue = 0;
      this.picture = null;
      this.imageData = event.target.files[0];
      this.onUpload();
    },
    onUpload() {
      this.picture = null;
      const storageRef = firebase
        .storage()
        .ref(`${this.imageData.name}`)
        .put(this.imageData);
      storageRef.on(
        `state_changed`,
        (snapshot) => {
          this.uploadValue =
            (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
        },
        (error) => {
          console.log(error.message);
        },
        () => {
          this.uploadValue = 100;
          storageRef.snapshot.ref.getDownloadURL().then((url) => {
            this.picture = url;
            this.userImage = url;
          });
        }
      );
    },
    submitFile() {
      const data = {
        name: this.userData.name,
        lastname: this.userData.lastname,
        profile_image: this.userImage,
        birth: this.userData.birth,
      };
      axios
        .put(
          SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/",
          data,
          null
        )
        .then(() => {
          axios
            .get(
              SERVER.URL + SERVER.ROUTES.mypage + sessionStorage.nickname + "/"
            )
            .then((res) => {
              this.userData = res.data;
              this.uploadValue = 0;
              this.userImage = res.data.profile_image;
              alert("프로필이미지가 변경되었습니다.");
            })
            .catch((err) => console.log(err));
        })
        .catch((err) => console.log(err));
    },
  },
  data() {
    return {
      gradeInfo: false,
      userData: "",
      userImage: "",
      imageData: null,
      picture: null,
      uploadValue: 0,
      file: "",
      selectedFile: null,
    };
  },
};
</script>

<style type="text/css" lang="scss">
@import "@/assets/css/components/mypage/mypageProfile.scss";
</style>
