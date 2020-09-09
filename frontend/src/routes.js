import Home from "@/views/Home.vue";
import Login from "@/views/Login";
import Community from "@/views/Community";
import Heritage from "@/views/Heritage";
import Maps from "@/views/Maps";
import Signup from "@/views/Signup";

export default [
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
    path: "/community",
    name: "Community",
    component: Community,
  },
  {
    path: "/maps",
    name: "Maps",
    component: Maps,
  },
  {
    path: "/login",
    name: "Login",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    // component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    component: Login,
  },
  {
    path: "/signup",
    name: "Signup",
    component: Signup,
  },
];
