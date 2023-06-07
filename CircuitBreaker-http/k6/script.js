import http from "k6/http";
import { check } from "k6";

export const options = {
    vus: 100,
    duration: "30s",
};
export default function () {
  const res = http.get("http://localhost:3000/");
  check(res, {
    "is status 200": (r) => r.status === 200,
  });
  console.log(JSON.stringify(res.body))
}