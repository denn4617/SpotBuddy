import React, {useEffect} from "react";
import axios from "axios";
import { Button, View, Text, StyleSheet, Dimensions } from "react-native";
import { useState } from "react/cjs/react.development";
import { Buttons } from "../styles";

const UsersScreen = ({ navigation }) => {
    const [users, setUsers] = useState([])

    const getUsers = async() => {
        try {
            await axios.get("http://172.20.10.7:5000/api/users")
                .then(response => {
                    setUsers(response.data);
                    console.log(response.data);
                })
                .catch(error => {
                    console.log('Error fetching and parsing data', error);
                });
        } catch (error) {
            console.log(error);
        }
    };

    useEffect(() => {
        getUsers();
    }, [])
    return (
        <View style={styles.screenContainer}>

            {users.map(user => {
                return (
                    <View style={styles.userContainer} key={user.user_id}>
                        <Text>{user.username}</Text>
                    </View>
                )
            })}


        </View>
    );
};
const styles = StyleSheet.create({
    screenContainer: {
        flex: 1,
        justifyContent: "space-between",
        // backgroundColor: "red",
        width: "100%",
        height: "100%",

    },
    userContainer: {
        flex: 0.1,
        marginTop: 100,
        borderBottomWidth: 1,
        borderTopWidth: 1,
        borderColor: "green",
        alignItems: "center",
        justifyContent: "center",
        // width: Dimensions.get("window").width,

    },
});
export default UsersScreen;
