import Vue from "vue";
import VueRouter from "vue-router";

import Home from "@/views/Home.vue";
import Login from "@/views/Login";
import Maps from "@/views/Maps";
import Mypage from "@/views/Mypage";
import Otherpage from "@/views/Otherpage";
import Signup from "@/views/Signup";
import Survey from "@/views/Survey";
import ProfileUpdate from "@/views/ProfileUpdate";

import Community from "@/views/Community";
import CommunityReviewItem from "@/components/community/CommunityReviewItem";

import Heritage from "@/views/Heritage";
import HeritageCardDetail from "@/components/heritage/HeritageCardDetail";
import HeritageSearchBar from "@/components/heritage/HeritageSearchBar";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/heritage",
    name: "Heritage",
    component: Heritage,
  },
  {
    path: "/heritage/:id",
    name: "HeritageCardDetail",
    component: HeritageCardDetail,
  },
  {
    path: "/heritage/search/",
    name: "HeritageSearchBar",
    component: HeritageSearchBar,
  },
  {
    path: "/community",
    name: "Community",
    component: Community,
  },
  {
    path: "/community/:id",
    name: "CommunityReviewItem",
    component: CommunityReviewItem,
  },
  {
    path: "/maps",
    name: "Maps",
    component: Maps,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
  {
    path: "/mypage",
    name: "Mypage",
    component: Mypage,
  },
  {
    path: "/otherpage/:nickname",
    name: "Otherpage",
    component: Otherpage,
  },
  {
    path: "/profileupdate",
    name: "ProfileUpdate",
    component: ProfileUpdate,
  },
  {
    path: "/survey",
    name: "Survey",
    component: Survey,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
