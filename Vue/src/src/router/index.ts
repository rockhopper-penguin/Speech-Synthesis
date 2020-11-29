import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Home from "../views/Home.vue";
import Result from "@/components/Result.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    name: "Home",
    component: Home
  },
  {
    path: "/result",
    name: "Result",
    component: Result
  }
];

const router = new VueRouter({
  routes
});

export default router;
