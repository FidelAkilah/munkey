// src/auth.ts
import NextAuth from "next-auth";
import Credentials from "next-auth/providers/credentials";

export const { handlers, auth, signIn, signOut } = NextAuth({
  providers: [
    Credentials({
      name: "MUN Account",
      credentials: {
        email: { label: "Email", type: "email" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        const res = await fetch("http://localhost:8000/auth/jwt/create/", {
          method: "POST",
          body: JSON.stringify(credentials),
          headers: { "Content-Type": "application/json" },
        });

        const tokens = await res.json();

        if (res.ok && tokens) {
          // Fetch user details with the new token
          const userRes = await fetch("http://localhost:8000/auth/users/me/", {
            headers: { Authorization: `Bearer ${tokens.access}` },
          });
          const user = await userRes.json();
          return { ...user, accessToken: tokens.access, refreshToken: tokens.refresh };
        }
        return null;
      },
    }),
  ],
callbacks: {
    async jwt({ token, user }) {
        if (user) return { ...token, ...user };
        return token;
    },
    async session({ session, token }: { session: any; token: any }) {
        session.user = token as any;
        return session;
    },
},
});