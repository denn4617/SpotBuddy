import React, { useEffect } from "react";
import axios from "axios";
import { View, Text, StyleSheet, SafeAreaView, FlatList } from "react-native";
import { useState } from "react/cjs/react.development";
import { Buttons } from "../styles";

const UsersScreen = ({ navigation }) => {
    const [users, setUsers] = useState([])

    const getUsers = async () => {
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
        <SafeAreaView style={styles.screenContainer}>

            {users.map(user => {
                return (
                    <View style={styles.userContainer} key={user.user_id}>
                        <Text>{user.username}</Text>
                    </View>
                )
            })}
            
            
            {/* {users.map(user => {
                return (
                    <View >
                        <FlatList
                            contentContainerStyle={styles.userContainer}
                            data={[
                                { key: user.user_id },
                            ]}
                            renderItem={({ user }) => <Text>{user.username}</Text>}
                            // keyExtractor={userID => user.user_id}
                        />
                    </View>
                )
            })}  */}




        </SafeAreaView>
    );
};
const styles = StyleSheet.create({
    screenContainer: {
        flex: 1,
        justifyContent: "flex-start",
        // backgroundColor: "red",
        width: "100%",
        height: "100%",

    },
    userContainer: {
        flex: 0.1,
        // borderBottomWidth: 1,
        // borderTopWidth: 1,
        borderColor: "green",
        alignItems: "center",
        justifyContent: "center",
        // width: Dimensions.get("window").width,

    },
});
export default UsersScreen;
