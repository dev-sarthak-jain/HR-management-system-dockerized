import React, { useEffect, useState } from "react";
// import promotionData from "../../mockups/Home/promotionData";
import AOS from "aos";
import "aos/dist/aos.css";

const Promotion = () => {
  const [isScrolled, setIsScrolled] = useState([true, false, false]);

  const handleScroll = () => {
        console.log(window.scrollY)
    if (window.scrollY >= 400 && window.scrollY <= 600) {
      setIsScrolled((prev) => {
         return [isScrolled[0] === true, isScrolled[1] === false, isScrolled[2] === false ]
      });
    }else if ((window.scrollY >= 650 && window.scrollY <= 850)) {
      setIsScrolled(() =>{
        return [isScrolled[0] === false, isScrolled[1] === true, isScrolled[2] === false ]

      });
    }
     else if (window.scrollY > 850) {
      setIsScrolled(() =>{
        return [isScrolled[0] === false, isScrolled[1] === false, isScrolled[2] === true ]
      });
    }

  };

  useEffect(() => {
    AOS.init({
      duration: 1000, // Duration of the animation
      once: true, // Animation only happens once
    });
  }, []);

  // Listen for scroll events
  useEffect(() => {
    window.addEventListener("scroll", handleScroll);

    return () => {
      window.removeEventListener("scroll", handleScroll);
    };
  }, []);








  return (
    // <div className="py-8 bg-backgroundColor">
    //   <div className="max-w-4xl mx-auto px-4">
    //     <h1 className="text-3xl font-bold mb-10">
    //       Our service allow you to...
    //     </h1>
    //     {promotionData.map((item, index) => (
    //       <PromotionItem key={index} {...item} />
    //     ))}
    //   </div>
    // </div>
    <div className="w-full bg-backgroundColor z-0 my-8">
      <div className="relative flex justify-between container py-7 md:py-10 ">


      <div className="lg:hidden">
      <h1 className="font-nunito italic font-bold sm:text-2xl md:text-3xl mb-4 text-white">
            Our services allow you to...
          </h1>
        <div
          className={`flex flex-wrap justify-start w-[95%] p-4 my-7 h-[180px]  ${isScrolled[0] ? "aos-init bg-greenOnDarkMode " : ""}`}
          data-aos="fade-up"
        >
            <h1 className="w-3/5 text-xl md:text-3xl lg:text-5xl font-semibold mr-2 text-white">Explore your interests. </h1>
            <p className="w-3/5 italic font-bold mt-2.5 sm:mt-6 sm:text-lg text-white">
            Browse policies based on your interest and generate new ones
            </p>
        </div>


        <div
          className={`flex flex-wrap justify-end ml-4 w-full p-4 my-7 h-[180px]   ${isScrolled[1] ?  "aos-init bg-greenOnDarkMode ": ""}`}
          data-aos="fade-up"
        >
            <h1 className="w-3/5 text-xl md:text-3xl lg:text-5xl font-semibold mr-2 text-white">Visualize your needs</h1>
            <p className="w-3/5 italic font-bold mt-2.5 sm:mt-6 sm:text-lg text-white">
            Interactive geographic representation of  policy cards and their trends
            </p>
        </div>

           <div
          className={`flex flex-wrap justify-start w-[95%] p-4 my-7 h-[180px] ${isScrolled[2] ?  "aos-init bg-greenOnDarkMode " : ""}`}
          data-aos="fade-up"
        >
            <h1 className="w-3/5 text-xl md:text-3xl lg:text-5xl font-semibold mr-2 text-white">Discuss with the community.</h1>
            <p className="w-3/5 italic font-bold mt-2.5 sm:mt-6 sm:text-lg text-white">
            Chat about the different policies created with others members
            </p>
        </div>
      </div>


        <div className="hidden lg:flex flex-col space-y-4 sm:ml-6 lg:mt-[190px]">
          <h1 className="font-nunito italic font-bold sm:text-2xl md:text-3xl mb-4 text-white">
            Our services allow you to...
          </h1>
          <div className="flex items-center">
            <h1 className="text-xl sm:text-5xl font-semibold mr-2 text-white">Engage. </h1>
            <span className="text-sm italic font-bold mt-4 sm:mt-6 sm:text-lg text-white">
            Foster a culture of engagement.
            </span>
          </div>
          <div className="flex items-center">
            <h1 className="text-xl sm:text-5xl font-semibold mr-2 text-white">Manage. </h1>
            <span className="text-sm italic font-bold mt-4 sm:mt-6 sm:text-lg text-white">
            Seamlessly handle all your HR tasks.
            </span>
          </div>
          <div className="flex items-center">
            <h1 className="text-xl sm:text-5xl font-semibold mr-1 text-white">Connect and Collaborate. </h1>
            <span className="text-sm italic font-bold mt-4 sm:mt-6 sm:text-lg text-white">
            Break down silos and encourage collaboration.
            </span>
          </div>
        </div>
        <svg
          className="hidden lg:block absolute mt-[600px] ml-[-20px]"
          width="25"
          height="25"
          viewBox="0 0 325 325"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="162.5" cy="162.5" r="162.5" fill="#474B7D"></circle>
        </svg>
        <svg
          className="hidden lg:block absolute mt-[620px] ml-[20px]"
          width="125"
          height="125"
          viewBox="0 0 325 325"
          fill="none"
          xmlns="http://www.w3.org/2000/svg"
        >
          <circle cx="162.5" cy="162.5" r="162.5" fill="#d9d9d9"></circle>
        </svg>
        <div className="hidden lg:block">
          <div className="flex-col">
            <svg
              className="mt-[-50px] mr-[250px]"
              width="325"
              height="325"
              viewBox="0 0 325 325"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle cx="162.5" cy="162.5" r="162.5" fill="#474B7D"></circle>
            </svg>
            <svg
              className="mt-[-230px] ml-[80px] absolute"
              width="147"
              height="139"
              viewBox="0 0 147 139"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clipPath="url(#clip0_718_879)">
                <path
                  d="M0 11.0571C0 4.94725 4.802 0 10.7188 0H87.2812C93.2041 0 98 4.94725 98 11.0571V71.0812C98 74.0137 96.8707 76.8261 94.8605 78.8997C92.8504 80.9733 90.124 82.1383 87.2812 82.1383H49.3736L33.6079 98.3953C32.3598 99.6821 30.77 100.558 29.0393 100.913C27.3086 101.268 25.5147 101.086 23.8844 100.389C22.2541 99.693 20.8606 98.5135 19.88 97.0002C18.8993 95.4869 18.3756 93.7077 18.375 91.8874V82.1383H10.7188C7.87596 82.1383 5.1496 80.9733 3.13945 78.8997C1.12929 76.8261 0 74.0137 0 71.0812L0 11.0571ZM10.7188 9.47749C10.3126 9.47749 9.92316 9.64391 9.63599 9.94014C9.34883 10.2364 9.1875 10.6381 9.1875 11.0571V71.0812C9.1875 71.9531 9.8735 72.6608 10.7188 72.6608H22.9688C24.1871 72.6608 25.3555 73.16 26.217 74.0487C27.0785 74.9374 27.5625 76.1427 27.5625 77.3995V91.2303L44.2225 74.0508C44.6481 73.6098 45.1539 73.2599 45.7111 73.0214C46.2682 72.7828 46.8655 72.6603 47.4688 72.6608H87.2812C87.6874 72.6608 88.0768 72.4943 88.364 72.1981C88.6512 71.9019 88.8125 71.5001 88.8125 71.0812V11.0571C88.8125 10.6381 88.6512 10.2364 88.364 9.94014C88.0768 9.64391 87.6874 9.47749 87.2812 9.47749H10.7188ZM136.281 47.3875H114.844C113.625 47.3875 112.457 46.8882 111.595 45.9995C110.734 45.1108 110.25 43.9055 110.25 42.6487C110.25 41.3919 110.734 40.1866 111.595 39.2979C112.457 38.4092 113.625 37.91 114.844 37.91H136.281C142.198 37.91 147 42.8635 147 48.967V108.991C147 111.924 145.871 114.736 143.861 116.81C141.85 118.883 139.124 120.048 136.281 120.048H128.625V129.797C128.624 131.618 128.101 133.397 127.12 134.91C126.139 136.423 124.746 137.603 123.116 138.299C121.485 138.996 119.691 139.178 117.961 138.823C116.23 138.468 114.64 137.592 113.392 136.305L97.6264 120.048H65.8438C63.001 120.048 60.2746 118.883 58.2644 116.81C56.2543 114.736 55.125 111.924 55.125 108.991V99.7348C55.125 98.478 55.609 97.2727 56.4705 96.384C57.332 95.4953 58.5004 94.9961 59.7188 94.9961C60.9371 94.9961 62.1055 95.4953 62.967 96.384C63.8285 97.2727 64.3125 98.478 64.3125 99.7348V108.991C64.3125 109.863 64.9985 110.571 65.8438 110.571H99.5312C100.75 110.571 101.92 111.07 102.778 111.961L119.438 129.14V115.309C119.438 114.053 119.921 112.847 120.783 111.959C121.644 111.07 122.813 110.571 124.031 110.571H136.281C136.687 110.571 137.077 110.404 137.364 110.108C137.651 109.812 137.812 109.41 137.812 108.991V48.967C137.812 48.5481 137.651 48.1463 137.364 47.8501C137.077 47.5539 136.687 47.3875 136.281 47.3875ZM76.7462 27.0424L46.1213 58.6341C45.696 59.0758 45.1902 59.4263 44.6331 59.6655C44.076 59.9047 43.4785 60.0278 42.875 60.0278C42.2715 60.0278 41.674 59.9047 41.1169 59.6655C40.5598 59.4263 40.054 59.0758 39.6287 58.6341L24.3162 42.8383C23.8899 42.3985 23.5518 41.8764 23.3211 41.3019C23.0904 40.7273 22.9716 40.1115 22.9716 39.4895C22.9716 38.8676 23.0904 38.2518 23.3211 37.6772C23.5518 37.1027 23.8899 36.5806 24.3162 36.1408C24.7426 35.7011 25.2487 35.3522 25.8056 35.1142C26.3626 34.8762 26.9596 34.7537 27.5625 34.7537C28.1654 34.7537 28.7624 34.8762 29.3194 35.1142C29.8763 35.3522 30.3824 35.7011 30.8088 36.1408L42.875 48.5816L70.2538 20.345C70.6801 19.9053 71.1861 19.5564 71.7431 19.3184C72.3001 19.0804 72.8971 18.9579 73.5 18.9579C74.1029 18.9579 74.6999 19.0804 75.2569 19.3184C75.8139 19.5564 76.3199 19.9053 76.7462 20.345C77.1726 20.7848 77.5107 21.3068 77.7414 21.8814C77.9721 22.456 78.0909 23.0718 78.0909 23.6937C78.0909 24.3156 77.9721 24.9315 77.7414 25.506C77.5107 26.0806 77.1726 26.6027 76.7462 27.0424Z"
                  fill="white"
                ></path>
              </g>
              <defs>
                <clipPath id="clip0_718_879">
                  <rect width="147" height="139" fill="white"></rect>
                </clipPath>
              </defs>
            </svg>
            <svg
              className="mt-[-150px] ml-[200px]"
              width="325"
              height="325"
              viewBox="0 0 325 325"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle cx="162.5" cy="162.5" r="162.5" fill="#B7BBE8"></circle>
            </svg>
            <svg
              className="mt-[-230px] ml-[300px] absolute"
              width="139"
              height="139"
              viewBox="0 0 139 139"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clipPath="url(#clip0_718_877)">
                <path
                  d="M0 27.8C0 17.3403 5.421 6.394 13.9 0C13.9 5.87275 18.6955 13.9 27.8 13.9C33.3298 13.9 38.633 16.0967 42.5432 20.0068C46.4533 23.917 48.65 29.2202 48.65 34.75C48.65 37.4327 48.1009 39.9764 47.1766 42.3324C52.3318 46.4238 57.4085 50.6131 62.404 54.898L47.9481 69.354C43.6648 64.3571 39.4756 59.2804 35.3825 54.1266C32.9699 55.0894 30.3976 55.5892 27.8 55.6C12.4405 55.6 0 43.1595 0 27.8ZM84.4564 75.3936L93.7763 66.0736C98.0922 68.2956 102.871 69.4694 107.725 69.5C116.02 69.5 123.975 66.205 129.84 60.3398C135.705 54.4746 139 46.5196 139 38.225C139 33.1862 137.693 28.488 135.574 24.2764L111.2 48.65L97.3 34.75L121.674 10.3764C117.358 8.15445 112.579 6.98062 107.725 6.95C99.4304 6.95 91.4754 10.245 85.6102 16.1102C79.745 21.9754 76.45 29.9304 76.45 38.225C76.45 43.2637 77.7566 47.9619 79.8764 52.1736L6.95 125.1L20.85 139L68.4436 91.4064C81.533 104.836 95.4039 117.482 109.984 129.277L119.887 137.262L130.312 126.837L122.327 116.934C110.532 102.354 97.8864 88.483 84.4564 75.3936Z"
                  fill="#E7EDFB"
                ></path>
              </g>
              <defs>
                <clipPath id="clip0_718_877">
                  <rect width="139" height="139" fill="#474B7D"></rect>
                </clipPath>
              </defs>
            </svg>
            <svg
              className="mt-[-90px] mr-[250px]"
              width="325"
              height="325"
              viewBox="0 0 325 325"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <circle cx="162.5" cy="162.5" r="162.5" fill="#868BC7"></circle>
            </svg>
            <svg
              className="mt-[-230px] ml-[80px] absolute"
              width="124"
              height="124"
              viewBox="0 0 124 124"
              fill="none"
              xmlns="http://www.w3.org/2000/svg"
            >
              <g clipPath="url(#clip0_718_875)">
                <path
                  d="M123.787 118.364C123.787 119.858 123.285 121.292 122.392 122.349C121.5 123.406 120.289 124 119.026 124H4.76103C3.49833 124 2.28734 123.406 1.39447 122.349C0.501607 121.292 0 119.858 0 118.364V5.63636C0 4.14151 0.501607 2.70788 1.39447 1.65085C2.28734 0.593831 3.49833 0 4.76103 0C6.02374 0 7.23473 0.593831 8.12759 1.65085C9.02046 2.70788 9.52207 4.14151 9.52207 5.63636V72.1243L39.713 40.8636C40.5345 40.0123 41.5783 39.521 42.6694 39.4723C43.7604 39.4235 44.8325 39.8202 45.7059 40.5959L80.7055 71.6734L115.89 35.2273C116.351 34.6867 116.901 34.2634 117.505 33.9836C118.11 33.7038 118.756 33.5732 119.405 33.6C120.054 33.6268 120.691 33.8104 121.278 34.1394C121.864 34.4685 122.388 34.936 122.816 35.5134C123.244 36.0908 123.569 36.7658 123.769 37.4968C123.968 38.2279 124.04 38.9997 123.979 39.7647C123.918 40.5298 123.725 41.2719 123.412 41.9455C123.1 42.6191 122.675 43.21 122.162 43.6818L84.0739 83.1364C83.2524 83.9877 82.2086 84.479 81.1175 84.5277C80.0265 84.5765 78.9544 84.1798 78.081 83.4041L43.0814 52.3407L9.52207 87.103V112.727H119.026C120.289 112.727 121.5 113.321 122.392 114.378C123.285 115.435 123.787 116.869 123.787 118.364Z"
                  fill="white"
                ></path>
              </g>
              <defs>
                <clipPath id="clip0_718_875">
                  <rect width="124" height="124" fill="white"></rect>
                </clipPath>
              </defs>
            </svg>
          </div>
        </div>
      </div>
    </div>
  );
};

// const PromotionItem = ({ icon, title, desc, btn }) => (
//   <div className="flex items-center justify-between bg-white mb-6">
//     <div className="flex items-center">
//       <div className="p-4 bg-cardBackground text-blue-800 flex items-center justify-center mr-4">
//         {icon}
//       </div>
//       <div className="ml-10">
//         <h1 className="text-2xl text-purpleCustom font-bold">{title}</h1>
//         <span className=" font-normal italic text-black">{desc}</span>
//       </div>
//     </div>
//     <button className="flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-blue-800 hover:scale-110">
//       {btn}
//     </button>
//   </div>
// );

export default Promotion;
