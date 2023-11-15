import { useQuery } from "@tanstack/react-query";
import { useParams } from "react-router-dom";
import { getRoom } from "./api";

export default function RoomDetail() {
  const { roomId } = useParams();
  const { isLoading, data } = useQuery([`room:${roomId}`], getRoom);
  return <h1>hello</h1>;
}
