import Cookie from "js-cookie";
import { QueryFunctionContext } from "@tanstack/react-query";
import axios from "axios";

const instance = axios.create({
  baseURL: "http://127.0.0.1:8000/api/v1/",
  withCredentials: true, // sends a cookie when fetching
});

export const getRooms = () =>
  instance.get("rooms/").then((response) => response.data);


export const getRoom = ({ queryKey }: QueryFunctionContext) => {
  // 전달받은 '쿼리 키'는 { queryKey } 프로퍼티명을 통해서 가져올 수 있음.
  console.log(queryKey); // ['rooms', '3']
  const [_, roomId] = queryKey;
  return instance.get(`rooms/${roomId}`).then((response) => response.data);
};


export const getRoomReviews = ({ queryKey }: QueryFunctionContext) => {
  const [_, roomId] = queryKey;
  return instance
    .get(`rooms/${roomId}/reviews`)
    .then((response) => response.data);
};





export const getMe = () =>
  instance.get(`users/me`).then((response) => response.data);


export const logOut = () =>
  instance
    .post(`users/log-out`, null, {
      headers: { "X-CSRFToken": Cookie.get("csrftoken") || "" },
    })
    .then((response) => response.data);




    

export const githubLogIn = (code: string) =>
  instance
    .post(
      `/users/github`,
      { code },
      { headers: { "X-CSRFToken": Cookie.get("csrftoken") || "" } }
    )
    .then((response) => response.status);
