import NextAuth from "next-auth";
import type { AuthOptions } from "next-auth";
import Credentials from "next-auth/providers/credentials";

const API_BASE = process.env.NEXT_PUBLIC_API_URL || "https://mun-global.onrender.com";

export const authOptions: AuthOptions = {
  secret: process.env.NEXTAUTH_SECRET,
  providers: [
    Credentials({
      name: "MUN Account",
      credentials: {
        username: { label: "Username", type: "text" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        if (!credentials?.username || !credentials?.password) {
          return null;
        }

        try {
          const res = await fetch(`${API_BASE}/auth/jwt/create/`, {
            method: "POST",
            body: JSON.stringify({
              username: credentials.username,
              password: credentials.password,
            }),
            headers: { "Content-Type": "application/json" },
          });

          if (!res.ok) {
            return null;
          }

          const tokens = await res.json();

          if (tokens.access) {
            const userRes = await fetch(`${API_BASE}/auth/users/me/`, {
              headers: { Authorization: `Bearer ${tokens.access}` },
            });
            
            if (!userRes.ok) {
              return null;
            }
            
            const user = await userRes.json();
            const role = user.is_superuser ? 'AD' : (user.role || 'SR');
            
            return { 
              id: user.id?.toString() || user.pk?.toString(),
              name: user.username,
              email: user.email || `${user.username}@example.com`,
              accessToken: tokens.access, 
              refreshToken: tokens.refresh,
              role: role,
              isSuperuser: user.is_superuser || false,
            };
          }
          return null;
        } catch (error) {
          console.error("Auth error:", error);
          return null;
        }
      },
    }),
  ],
  pages: {
    signIn: "/login",
  },
  session: {
    strategy: "jwt",
    maxAge: 24 * 60 * 60,
  },
  cookies: {
    sessionToken: {
      name: process.env.NODE_ENV === "production"
        ? "__Secure-next-auth.session-token"
        : "next-auth.session-token",
      options: {
        httpOnly: true,
        sameSite: "lax",
        path: "/",
        secure: process.env.NODE_ENV === "production",
      },
    },
  },
  callbacks: {
    async jwt({ token, user }) {
      if (user) {
        token.accessToken = (user as { accessToken?: string }).accessToken || "";
        token.refreshToken = (user as { refreshToken?: string }).refreshToken || "";
        token.role = (user as { role?: string }).role || 'SR';
        token.isSuperuser = (user as { isSuperuser?: boolean }).isSuperuser || false;
        token.id = (user as { id?: string }).id || "";
      }
      return token;
    },
    async session({ session, token }) {
      if (token) {
        session.user = {
          ...session.user,
          id: token.id as string,
          accessToken: token.accessToken as string,
          refreshToken: token.refreshToken as string,
          role: (token.role as string) || 'SR',
          isSuperuser: (token.isSuperuser as boolean) || false,
        };
      }
      return session;
    },
  },
  debug: process.env.NODE_ENV !== "production",
};

const handler = NextAuth(authOptions);

export { handler as GET, handler as POST };

