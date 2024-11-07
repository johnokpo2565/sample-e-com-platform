import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import DashboardView from "../views/DashboardView.vue";
import LoginView from "../views/LoginView.vue";
import SignUpView from "../views/SignUpView.vue";
import { userAuthStore } from "../stores/authStore";
import { computed } from "vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },

    {
      path: "/login",
      name: "login",
      component: LoginView,
    },

    {
      path: "/dashboard",
      name: "dashboard",
      component: DashboardView,
      meta: { requiresAuth: true },
    },

    {
      path: "/signup",
      name: "signup",
      component: SignUpView,
    },

    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
  ],
});

router.beforeEach((to, from, next) => {
  const auth = userAuthStore();
  const loggedIn = !!auth.accessToken;
  if (to.meta.requiresAuth) {
    if (loggedIn) {
      next();
    } else {
      next("/login");
    }
  } else {
    if (loggedIn && to.path === "/login") {
      next("/dashboard");
    } else {
      next();
    }
  }
});
// router.beforeEach((to, from, next) => {
//   const loggedIn = "";

//   if (to.meta.requresAuth) {
//     if (loggedIn) {
//       next();
//     } else {
//       next("/");
//     }
//   } else {
//     if (loggedIn && to.path === "/") {
//       next("/dashboard");
//     } else {
//       next("/");
//     }
//   }
// });

export default router;
