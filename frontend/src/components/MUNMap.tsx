"use client";
import { APIProvider, Map, Marker } from "@vis.gl/react-google-maps";

// eslint-disable-next-line @typescript-eslint/no-explicit-any
export default function MUNMap({ markers }: { markers: any[] }) {
  const apiKey = process.env.NEXT_PUBLIC_GOOGLE_MAPS_API_KEY || "YOUR_KEY";

  return (
    <div className="h-[450px] w-full rounded-3xl overflow-hidden border border-slate-200">
      <APIProvider apiKey={apiKey}>
        <Map
          defaultCenter={{ lat: 20, lng: 0 }}
          defaultZoom={2}
          mapId="MUN_HUB_MAP"
        >
          {markers.map((conf) => (
            <Marker 
              key={conf.id} 
              position={{ lat: conf.latitude, lng: conf.longitude }} 
              label={conf.name}
            />
          ))}
        </Map>
      </APIProvider>
    </div>
  );
}