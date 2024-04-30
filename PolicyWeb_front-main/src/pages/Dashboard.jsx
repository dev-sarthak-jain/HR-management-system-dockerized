import React, { useEffect, useState } from 'react';
import DashHeader from "../components/Dashboard/DashHeader"
import DashMapSearchPanel from "../components/Dashboard/DashMapSearchPanel"
import DashCardPanel from "../components/Dashboard/DashCardPanel"
import { useDispatch, useSelector } from 'react-redux';
import { get_all_policy_card_API, get_all_policy_card_by_location_API } from '../redux/Thunks/policyCardThunk';
import { AiFillCaretDown, AiFillCaretUp } from "react-icons/ai"
import Footer from '../layout/Footer';
import { userInfo } from '../redux/Selectors/selectors';
import { policySearchedLocation } from '../redux/Slices/sharedUseEffectSlice';


const Dashboard = () => {
    const dispatch = useDispatch()
    const [hideMap, setHideMap] = useState(true)
    const user = useSelector(state => userInfo(state))
    const location = useSelector(policySearchedLocation)

    const toggleMap = () => {
        setHideMap(!hideMap)
    }

    function getCardsFromServer(searchedParameter){
        if(searchedParameter === ""){
            // Get all Policy cards by the current user location
            dispatch(
            get_all_policy_card_by_location_API({
                location:user.state
            })
        )
        }else{
            // If user uses location search which means
            // they are interested in other locations
            // Get all policy cards from database
            dispatch(
                get_all_policy_card_API()
            )
        }
    }
    useEffect(() => {
        getCardsFromServer(location)
          // eslint-disable-next-line react-hooks/exhaustive-deps
    }, [location])



    return (
        <div>
            <DashHeader />
            <main className='lg:flex mx-7 pt-5 md:pt-10 lg:pt-20 border-t-2 border-[#000000BF]'>
            <div className='flex md:hidden justify-between flex-wrap'>
            <div className='w-[65%] flex '>
            <h1 className='py-2 pl-5 text-white font-nunito text-lg not-italic font-bold leading-normal'>
                Trending Policies
            </h1>
            </div>
            <div
            className={`w-[33%] ${!hideMap && "bg-[#284B63]" } flex justify-end py-2.5`}
            onClick={toggleMap}
            >
            <h1 className='text-white font-nunito text-sm  not-italic font-bold leading-normal'>
                Filter By
            </h1>
            {hideMap ?
            <AiFillCaretDown className="ml-1 text-white" />
            :
            <AiFillCaretUp className="ml-1 text-white" />
            }
            </div>
            </div>
                <aside className='w-full lg:w-[35%] mr-20 mb-10'>
                    <DashMapSearchPanel hideMap={hideMap} />
                </aside>
                <aside className='my-4 lg:my-0 w-full lg:w-[65%]'>
                    <DashCardPanel />
                </aside>
            </main>
            <Footer />
        </div>
    );
};

export default Dashboard;
