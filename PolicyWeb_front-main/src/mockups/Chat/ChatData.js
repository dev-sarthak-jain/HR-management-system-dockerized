import React from "react";
import { PiPencilSimpleLineThin } from "react-icons/pi";
import { FaSearch } from "react-icons/fa";
import { BsChatRightDots } from "react-icons/bs";

const chatData = [
  {
    icon: <FaSearch className="mx-auto" />,
    mainPrompt: "Discover",
    prompt1: "Tell me about Neural Niti",
    prompt2: "Tell me more about gun control policies",
  },
  {
    icon: <PiPencilSimpleLineThin className="mx-auto" />,
    mainPrompt: "Generate",
    prompt1:
      "Generate a policy that protects the rights of international unemployed workers",
    prompt2: "Generate a policy based on our conversation today",
  },
  {
    icon: <BsChatRightDots className="mx-auto" />,
    mainPrompt: "Chats",
    prompt1: "Here are my concerns, are there existing policies to help me?",
    prompt2: "Let’s talk policies today!",
  },
];

export default chatData;
