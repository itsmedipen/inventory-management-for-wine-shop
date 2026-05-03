# Wine Cellar POS — Complete Demo Guide

Everything you need to deploy, test, and demo this app to your client.

---

## Part 1 — Get the app onto your phone (5 minutes)

The recommended path is **Netlify Drop**. It's free, no signup, gives you an HTTPS link that works on any phone, and the camera barcode scanner will work properly.

### Step-by-step: Netlify Drop

1. On your PC, open https://app.netlify.com/drop in Chrome
2. Open File Explorer and go to `C:\Users\Dell\Documents\Claude\Projects\Inventory management system for Wine Shop`
3. Drag the file `WineShopPOS.html` onto the Netlify Drop page
4. Wait ~10 seconds. You'll get a link like `https://radiant-fox-abc123.netlify.app`
5. Click the link to verify it loads
6. To get a clean URL, rename the file to `index.html` before dropping (so the link works without `/WineShopPOS.html` at the end)

### Open on your phone

1. Send the Netlify link to your phone via WhatsApp, Telegram, or copy-paste it
2. Open the link in **Chrome** (Android) or **Safari** (iPhone)
3. Tap the menu and choose "Add to Home Screen" — now it looks like a real app
4. The first time you open the scanner, the browser will ask for camera permission. Tap "Allow"

### Sharing with your client

You can send the same Netlify link to your client. They can open it on their phone and try the app themselves before your meeting — this builds trust.

---

## Part 2 — First-time login

The login screen has two demo accounts pre-loaded. **Tap one of the demo cards** and the form auto-fills.

| Account  | Email                      | PIN  | Use for                                       |
| -------- | -------------------------- | ---- | --------------------------------------------- |
| Owner    | owner@wineshop.com         | 1234 | Full access — settings, audit logs, all data  |
| Cashier  | cashier@wineshop.com       | 0000 | Limited access — POS only, no settings/audit  |

For the demo, sign in as **Owner** so the client sees the full system.

---

## Part 3 — Module walkthrough

Here's what each section does and how to use it.

### Home (dashboard)

This is the landing screen after login. It shows:

- **Today's Sales** card — revenue, order count, items sold, profit
- **Quick action tiles** — New Sale, Scan Barcode, Add Stock, Reports
- **7-day trend** bar chart
- **Low stock alerts** — products at or below their threshold
- **Inventory snapshot** — total SKUs and stock value at cost

The numbers are real — they reflect everything you've sold and stocked in the demo.

### Sell (POS)

Bottom tab → **Sell**

Three ways to add a product to cart:

1. Tap any product tile in the grid
2. Type the name or barcode in the search bar at the top
3. Tap the **scan icon** (top right of search) and point at a barcode

Use the category chips (All / Whisky / Beer / Vodka / Rum / Wine) to filter quickly.

When the cart has items, a **brand-red bar appears at the bottom** showing total — tap it to go to checkout.

### Checkout

The checkout screen lets you:

- Adjust quantities with the +/− buttons
- Remove items with the trash icon
- Enter a customer name (optional — defaults to "Walk-in")
- Apply a discount in NPR
- Choose payment method: **Cash** or **QR / Mobile**

Tap **Complete Sale**:
- Cash → goes straight to the receipt
- QR → shows a payment QR popup; tap "Mark as paid" once your customer confirms

After completion, stock is deducted automatically and a receipt is generated.

### Receipt

Looks like a real thermal printer slip. You can:

- **Print** — opens the browser print dialog (works with any Bluetooth thermal printer or a normal printer)
- **Share** — uses the phone's share sheet (WhatsApp the receipt to the customer) or copies to clipboard
- **New sale** — starts a fresh transaction

### Stock (Products)

Bottom tab → **Stock**

Shows every product with stock levels color-coded:
- **Green badge** — healthy stock
- **Amber badge** — low stock
- **Red badge** — out of stock

Filter chips at the top: **All / Low stock / Out of stock**.

Tap any product to see its detail page with sales history, profit margin, and stock value.

The **red + button (bottom right)** opens the new product form.

### New / edit product

Required fields are starred. The form has three sections:

1. **Identity** — name, barcode (scan or type), category, unit, brand
2. **Pricing** — cost (what you pay supplier) and sell price (what customer pays)
3. **Stock** — opening stock count and low-stock alert threshold

Tap the **scan icon** next to the barcode field to scan instead of typing.

If a barcode you scan doesn't exist, the app will offer to **create a new product with that barcode pre-filled** — this is the workflow for adding new products as they arrive.

### Reports

Bottom tab → **Reports**

Toggle between **Today / 7 Days / 30 Days** at the top. You'll see:

- Revenue and profit cards
- Cash vs QR payment split
- Sales trend line chart
- Top 5 selling products
- Stock health bar (healthy / low / out)
- **Export sales as CSV** button — downloads a spreadsheet you can open in Excel

### More menu

Bottom tab → **More**

Contains:

- **Sales history** — all transactions grouped by date, tap any to view its receipt
- **Purchase entry** — record new stock from suppliers
- **Audit logs** (Owner only) — every login, sale, product change tracked with timestamp
- **Settings** (Owner only) — shop name, address, phone, PAN/VAT, tax rate, QR label, demo reset

### Recording a purchase

When new stock arrives:

1. More → Purchase entry → "Record new purchase"
2. Enter supplier name
3. Tap **Add** to create line items
4. For each line: pick the product, enter quantity, enter cost per unit
5. Tap **Receive stock** — inventory increases and the latest cost updates

### Audit log

Every action is recorded. The log shows: who did it, what they did, and when. This is your **trust feature** — show this to the client to prove nothing can be hidden.

### Settings

Edit your shop details (these print on receipts), change tax rate (Nepal VAT is 13% if applicable), update the QR label (Fonepay / eSewa / Khalti), and adjust the default low-stock threshold.

The **danger zone** at the bottom resets all data back to demo defaults — useful before showing the demo again to look fresh.

---

## Part 4 — Demo script for your client meeting

Use this exact order. It builds a story: **shop overview → daily work → trust → reports**. Total time: about 8–10 minutes.

### Before the meeting

1. Open Settings → tap **Reset demo data**. The dashboard now looks fresh with the seeded data
2. Make sure your phone is fully charged and connected to Wi-Fi
3. Have a real product with a barcode handy (any wine bottle from the shop) — for the live scan

### The walkthrough (in this order)

**1. Open the login screen** (10 seconds)
> "This is your shop's POS. You can use it on any phone, tablet, or computer. Each staff member has their own login."

Tap the Owner demo account, sign in.

**2. Show the dashboard** (1 minute)
> "When you open the app each morning, you see exactly how your shop is doing — today's sales, profit, items moving, and stock that needs reordering."

Point at the chart, point at the low-stock alerts.

**3. Make a sale** (3 minutes — this is the main act)
> "Now let's see how a sale works. A customer walks in with a bottle of Khukri Rum."

- Tap **Sell**
- Tap the scan icon
- **Scan a real bottle's barcode** in front of the client. (Or use the manual entry: `8901234500011`)
- Show how the product is instantly added
- Tap a couple more products to add them
- Tap the bottom bar to go to checkout
- Adjust a quantity, add a small discount
- Choose **QR payment** → show the QR code → "Mark as paid"
- Show the receipt
- Tap **Print** to show it can print, then **Share** to show it can WhatsApp

**4. Add a new product** (1 minute)
> "What if a new brand arrives that's not in your system?"

- Tap **Stock** → red + button
- Or, scan an unknown barcode and let the app prompt to create new
- Fill in: name, category, cost, price, opening stock
- Save → show it now appears in the list

**5. Add stock from a supplier** (1 minute)
> "When new stock arrives from your distributor, you record it here so your inventory stays accurate."

- More → Purchase entry → New purchase
- Add 2–3 lines, save
- Go back to Stock and show the inventory has gone up

**6. Reports** (1 minute)
> "At the end of the day, week, or month, you'll know exactly how your shop is performing."

- Tap **Reports**
- Switch between Today / 7 Days / 30 Days
- Point at top sellers, profit margin, payment split
- Tap **Export CSV** to show data can leave the app

**7. Audit log — the trust feature** (1 minute)
> "Every action — every sale, every product change, every login — is recorded. So if something looks wrong, you can see exactly what happened, who did it, and when. Nothing can be hidden."

- More → Audit logs
- Scroll through

**8. Wrap up** (30 seconds)
> "Everything you've seen — sales, stock, reports, receipts — works on any phone. Your staff use this same app on their phones. You can check on the shop from home. The data is safe, the actions are tracked, and you'll never lose track of inventory or sales again."

---

## Part 5 — Likely client questions and how to answer them

**"Can my staff steal money or fake sales?"**
Every transaction is logged with the cashier's name, time, and items. The audit log can't be edited. You'll see if anything is off.

**"What if the internet goes down?"**
The app works offline. It syncs when the connection comes back. (Note: in the production version with Supabase — for the demo it's all on-device.)

**"Can I print receipts?"**
Yes — any Bluetooth thermal printer works, or a normal printer. You can also send receipts via WhatsApp.

**"What about Fonepay / eSewa / Khalti?"**
The app currently records QR payments — you display your shop's static QR (printed once and pasted on the counter), customer pays, you mark it as paid. We can integrate live payment confirmation later if you want.

**"Will it work on cheap phones?"**
Yes. The app is lightweight — works on any Android phone made in the last 5 years.

**"Can I add more cashiers / branches?"**
Yes. We can add unlimited staff accounts with role-based access. Multiple branches is also possible.

**"How much does this cost to run?"**
The app itself is one-time. You'll need a Supabase database (~free for small shops, around $25/month if you grow), and optional hosting (~$0–10/month). I'll give you exact numbers in the proposal.

**"What if I want to change something later?"**
That's the whole point — I built this for you, so changes are easy. Just tell me what you need.

---

## Part 6 — Troubleshooting

**Camera doesn't open when I tap scan**
- Make sure you're on the HTTPS Netlify link, not the file:// link
- Tap "Allow" when the browser asks for camera permission
- On iPhone, you must use Safari (not Chrome) for camera in some cases
- Use the manual barcode entry as a fallback — type `8901234500011`

**Data disappeared / I want to start over**
- More → Settings → Reset demo data
- Or: clear browser data for the site

**The app looks small / not like a phone app on my computer**
- The app is mobile-first. On desktop, it shows in a 480px-wide centered column to look like a phone
- This is intentional — it's the same look users will see on their phone

**Receipt doesn't print**
- Make sure your printer is turned on and connected
- For thermal printers: pair via Bluetooth first, then use the browser's print dialog
- The demo's print uses the browser's native print — it works with any printer your phone supports

**I want to show this to a client but my data is messy from testing**
- Settings → Reset demo data
- This restores the original 16 products and a clean 7-day sales history

---

## Part 7 — What's a demo and what's "real"

This is a **fully functional demo**. Everything works — sales, stock, reports, audit, receipts. The data persists in your phone's browser storage so the demo behaves like a real app between sessions.

What's different from the production version we'd build for the client:

| Demo (this file)        | Production (React Native + Supabase) |
| ----------------------- | ------------------------------------ |
| Browser storage         | Cloud database (Supabase Postgres)   |
| One device              | Multi-device, real-time sync         |
| Web app                 | Native Android/iOS app               |
| Static QR only          | Optional Fonepay live integration    |
| Single shop             | Multi-branch, multi-staff            |

The UI, screens, and flows in the demo are exactly what the production app will look like — so what your client approves is what they get.

---

## Quick reference — demo cheat sheet

- **Login**: owner@wineshop.com / 1234
- **Sample barcodes**: `8901234500011` Khukri Rum, `8901234500028` Ruslan Vodka, `8901234500080` Old Durbar Whisky
- **Reset demo**: More → Settings → Reset demo data
- **Best demo path**: Login → Dashboard → Scan & sell → Receipt → Add product → Add stock → Reports → Audit log

Good luck with the demo — you've got this.
