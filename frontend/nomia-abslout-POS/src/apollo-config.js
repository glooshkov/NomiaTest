import {
  ApolloClient,
  InMemoryCache,
} from "@apollo/client/core";
import { createApolloProvider } from "@vue/apollo-option";
import { setContext } from "@apollo/client/link/context";
import createUploadLink from "apollo-upload-client/createUploadLink.mjs";

const httpLink = createUploadLink({
  uri: "http://127.0.0.1:8000/graphql",
});

const authLink = setContext((_, { headers }) => {
  const token = localStorage.getItem("token");
  return {
    headers: {
      ...headers,
      authorization: token || "",
    },
  };
});

export const apolloClient = new ApolloClient({
  link: authLink.concat(httpLink),
  cache: new InMemoryCache(),
});

export const apolloProvider = createApolloProvider({
  defaultClient: apolloClient,
});