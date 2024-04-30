import React from "react";
import { AvatarSlide, FAQs, Promotion, MediaBoard, Brand } from "../components";
// import TeamInfo from "../components/Home/TeamInfo";

const Home = () => {
  return (
    <div>
      <Brand />
      {/* <MediaBoard /> */}
      <Promotion />
      {/* <AvatarSlide /> */}
      <FAQs />
    </div>
  );
};

export default Home;
